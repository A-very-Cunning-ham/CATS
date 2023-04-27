import sys

import torch

import detection
# import cv2
from pathlib import Path
import os
from tqdm import tqdm
import numpy as np
import glob
# import torch
import torchvision
# from torchvision.io import VideoReader, read_video, read_video_timestamps
import torchvision.transforms.functional as TF
from collections.abc import Iterable
from queue import Queue
from threading import Thread, Lock
import json
from bson.objectid import ObjectId
from datetime import datetime

SENTINEL = "SENTINEL"
decoded_image_queue = Queue(maxsize=50)
model_results_queue = Queue(maxsize=50)
mongo_json_queue = Queue(maxsize=50)
MODE_ARGUMENT_INDEX = 1
MODE = sys.argv[MODE_ARGUMENT_INDEX].lower()
if MODE != "image" and MODE != "video":
    print(f"argument {MODE_ARGUMENT_INDEX} must be 'image' or 'video'")
    quit(-1)
# torchvision.set_video_backend("video_reader")
device = torch.device("cuda")


def decode_and_resize_images_loop(file_list: Iterable, pbar=None):
    current_image = 0
    for file_name in file_list:
        # if current_image > 500:
        #     break
        media_filepath = Path(file_name)
        split_filepath = list(os.path.splitext(os.path.basename(media_filepath)))
        if False:  # and glob.glob(f"{split_filepath[0]}-*-*.jpg"):
            continue
        if MODE == 'image':
            buff = torchvision.io.read_file(str(media_filepath))
            image_decoded = detection.decode_image(buff, force_cpu_decode=True)
            images_decoded = [image_decoded]
        else:
            images_decoded = detection.decode_video(media_filepath)
        file_stat = os.stat(media_filepath)
        for i, image_decoded in enumerate(images_decoded):
            this_image_split_filepath = f"{str(int(file_stat.st_mtime))}-{split_filepath[0]}"
            if MODE == "video":
                this_image_split_filepath += f"-{i:06}"
            img_og = image_decoded
            # image_decoded = letterbox(image_decoded, 640, stride=32)[0] Replace with:
            colors, height, width = image_decoded.shape
            pad_amount = int(abs(height - width) / 2)
            padding_amount = (0, pad_amount) if width > height else (pad_amount, 0)
            image_decoded = torchvision.transforms.Pad(padding=padding_amount, fill=114)(image_decoded)
            image_decoded = torchvision.transforms.Resize((640, 640))(image_decoded)
            image_decoded = image_decoded.to(device)
            decoded_image_queue.put(([this_image_split_filepath, split_filepath[1]], image_decoded, img_og))
            current_image += 1
        with pbar_lock:
            pbar.update()
    decoded_image_queue.put((SENTINEL, None, None))


def process_images_model_loop():
    while True:
        split_filepath, decoded_image, original_image = decoded_image_queue.get()
        if split_filepath == SENTINEL:
            break
        model_processed_image, pred = detection.run_model_on_image(decoded_image)
        decoded_image_queue.task_done()
        model_results_queue.put((split_filepath, model_processed_image, original_image, pred))
    model_results_queue.put((SENTINEL, None, None, None))  # Signal model threads to stop
    decoded_image_queue.put((SENTINEL, None, None, None))  # Signal other threads to stop


pbar_lock = Lock()


def process_model_results_loop(pbar=None):
    global output_folder, model_results_queue, mongo_json_queue
    while True:
        split_filepath, model_processed_image, img_og, pred = model_results_queue.get()

        if split_filepath == SENTINEL:
            break
        face_count = ear_count = 0
        image, objects_detected = detection.process_model_output(model_processed_image, img_og, pred,
                                                                 return_original=True)
        if len(objects_detected) == 0:
            continue
        filename = f"{split_filepath[0]}-Full-{ear_count:02}.jpg"
        mongo_json_queue.put((filename, objects_detected))
        #  TODO: Use nvJPEG
        out_jpeg_buffer = torchvision.io.encode_jpeg(image)
        torchvision.io.write_file(str(output_folder.joinpath(filename)), out_jpeg_buffer)
        for object_detected in objects_detected:
            # Note: Top Left = (0,0)
            if object_detected["confidence"] < 0.7:
                continue
            box_left_top = object_detected["left-top"]
            box_right_bottom = object_detected["right-bottom"]
            box_width = box_right_bottom[1] - box_left_top[1]
            box_height = box_right_bottom[0] - box_left_top[0]
            height_offset = int(box_height * 0.10)  # add 10% offset to top and bottom
            width_offset = int(box_width * 0.10)  # add 10% offset to left and right
            img_size = image.shape[1:]
            box_left = max(box_left_top[0] - width_offset, 0)
            box_top = max(box_left_top[1] - height_offset, 0)
            box_right = min(box_right_bottom[0] + width_offset, img_size[1])
            box_bottom = min(box_right_bottom[1] + height_offset, img_size[0])
            # cropped_image = image[box_left:box_right, box_top:box_bottom]
            cropped_image = TF.crop(image, top=box_top, left=box_left,
                                    height=box_bottom - box_top, width=box_right - box_left)
            if object_detected['class'] == 'Cat Face':
                filename = f"{split_filepath[0]}-{object_detected['class']}-{face_count:02}.jpg"
                face_count += 1
            elif object_detected['class'] == 'Cat Ear':
                filename = f"{split_filepath[0]}-{object_detected['class']}-{ear_count:02}.jpg"
                ear_count += 1
            else:
                print(
                    f"Exception: Object {object_detected['class']} is not one of the accepted classes (file: {split_filepath[0] + split_filepath[1]})")
                filename = f"{split_filepath[0]}-{object_detected['class']}(Unknown)-{ear_count:02}.jpg"
                print(f"\tFilename:{filename}.jpg")

            #  TODO: Use nvJPEG
            out_jpeg_buffer = torchvision.io.encode_jpeg(cropped_image.to('cpu'))
            torchvision.io.write_file(str(output_folder.joinpath(filename)), out_jpeg_buffer)
        model_results_queue.task_done()
    model_results_queue.put((SENTINEL, None, None, None))  # Signal other threads to stop
    mongo_json_queue.put((SENTINEL, None))


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def write_mongo_json_loop():
    global output_folder, mongo_json_queue
    with open(output_folder.joinpath("mongo_output.json"), 'w') as json_file:
        json_file.write("[\n")
        while True:
            filename, objects_detected = mongo_json_queue.get()
            if filename == SENTINEL:
                break
            filename_parts = os.path.basename(filename).split("-")
            FRAMERATE = 15
            image_timestamp = datetime.fromtimestamp(int(filename_parts[0]) + int(filename_parts[-3]) / FRAMERATE)
            mongo_object = {'_id': ObjectId.from_datetime(image_timestamp)[:8] + ObjectId()[8:], 'camera': "test-camera",
                            'filename': f"/images/{os.path.basename(filename)}",
                            'object-detected': "cat", 'catIDs': [], 'objects-found': objects_detected}
            json_file.write(json.dumps(mongo_object, cls=JSONEncoder))
            json_file.write(",\n")
        json_file.write("\n]")
    mongo_json_queue.put((SENTINEL, None))


output_folder = Path(r"E:/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/")
# output_folder = Path(r"/mnt/e/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/")


# TODO: REMOVE DO NOT USE
def old_main_process():
    global output_folder
    image_filepaths = Path(r"E:/Datasets/CatsAdrianVideos/trail cam footage").rglob("*.avi")
    current_image = 0
    for image_filepath in tqdm(np.fromiter(image_filepaths, dtype=object)):
        if current_image > 50:
            break
        current_image += 1
        image_filepath = Path(image_filepath)
        # with open(image_filepath, 'rb') as image_file:
        #     buff = image_file.read()
        # Replaced by:
        buff = torchvision.io.read_file(str(image_filepath))
        subimages = []
        split_filepath = os.path.splitext(os.path.basename(image_filepath))
        face_count = ear_count = 0

        # if glob.glob(f"{split_filepath[0]}-*-*.jpg"):
        #     continue

        objects_detected, image = detection.process_image(buff, return_original=True)
        for object_detected in objects_detected:
            # Note: Top Left = (0,0)
            if object_detected["confidence"] < 0.3:
                continue
            box_left_top = object_detected["left-top"]
            box_right_bottom = object_detected["right-bottom"]
            width = box_left_top[0] - box_right_bottom[0]
            height = box_left_top[1] - box_right_bottom[1]
            height_offset = int(height * 0.10)  # add 10% offset to top and bottom
            width_offset = int(width * 0.10)  # add 10% offset to left and right
            img_size = image.shape
            left_of_segment = max(box_left_top[0] - width_offset, 0)
            top_of_segment = max(box_left_top[1] - height_offset, 0)
            right_of_segment = min(box_right_bottom[0] + width_offset, img_size[1])
            bottom_of_segment = min(box_right_bottom[1] + height_offset, img_size[0])
            # cropped_image = image[left_of_segment:right_of_segment, top_of_segment:bottom_of_segment]
            cropped_image = TF.crop(image, top=top_of_segment, left=left_of_segment,
                                    height=bottom_of_segment - top_of_segment, width=right_of_segment - left_of_segment)
            if object_detected['class'] == 'Cat Face':
                filename = f"{split_filepath[0]}-{object_detected['class']}-{face_count:02}.jpg"
                face_count += 1
            elif object_detected['class'] == 'Cat Ear':
                filename = f"{split_filepath[0]}-{object_detected['class']}-{ear_count:02}.jpg"
                ear_count += 1
            else:
                print(
                    f"Exception: Object {object_detected['class']} is not one of the accepted classes (file: {image_filepath})")

            #  TODO: Use nvJPEG
            out_jpeg_buffer = torchvision.io.encode_jpeg(cropped_image.to('cpu'))
            torchvision.io.write_file(str(output_folder.joinpath(filename)), out_jpeg_buffer)
            # cv2.imwrite(str(output_folder.joinpath(filename)), cropped_image)
            # print(filename)


def main():
    threads: list[Thread] = []
    image_filepaths = Path(r"E:/Datasets/CatsAdrianVideos/trail cam footage").rglob("*.AVI")
    # image_filepaths = Path(r"/mnt/e/Datasets/CatsAdrianVideos/trail cam footage").rglob("*.AVI")
    file_paths = [file for file in image_filepaths if file.is_file()]
    image_filepaths = np.array(file_paths, dtype=object)
    pbar = tqdm(total=len(image_filepaths))
    print = pbar.write
    threads.append(Thread(target=decode_and_resize_images_loop, args=(image_filepaths,pbar)))
    threads.append(Thread(target=process_images_model_loop))
    for _ in range(2):
        threads.append(Thread(target=process_model_results_loop, args=(pbar,)))
    threads.append(Thread(target=write_mongo_json_loop))
    for i, t in enumerate(threads):
        t.start()
        print(f"Started thread {i}")
    for i, t in enumerate(threads):
        t.join()
        print(f"Joined thread {i}")
    print("Done")


if __name__ == "__main__":
    main()
