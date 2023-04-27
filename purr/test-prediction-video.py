import time
import detection
import cv2
import utils
import models
import glob
import os
# import pymongo
from bson.objectid import ObjectId
import json
import numpy as np
import sys
from pathlib import Path
from torchvision.io import VideoReader, read_video, read_video_timestamps, write_jpeg

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


files = glob.glob(sys.argv[1])
outpu_folder = Path(sys.argv[2])
with open("faked-json-mongo-video.json", 'w') as json_file:
    json_file.write("[")
    for i, filename in enumerate(files):
        if i > 20:
            break
        timestamps = read_video_timestamps(filename, 'sec')
        video_frames = read_video(filename)
        with open(filename, 'rb') as video_file:
            buff = video_file.read()
            objects_detected, image = detection.process_image(buff)
            newID = ObjectId()
            timeObjectID = ObjectId.from_datetime(timestamps[0])
            finalID = timeObjectID[:8] + newID[8:]
            mongo_object = {'_id': finalID, 'camera': "test-camera", 'filename': f"/images/{os.path.basename(filename)}",
                            'object-detected': "cat", 'catIDs': [], 'objects-found': objects_detected}
            json_file.write(json.dumps(mongo_object, cls=JSONEncoder))
            json_file.write(",")
            # image = image[0][::-1, :, :].transpose(1, 2, 0)
            path_basename = os.path.basename(filename)
            with open(path_basename, "wb") as image_file_out:
                image_encode_out = cv2.imencode('.jpg', image)[1]
                img_encode = image_encode_out
                data_encode = np.array(img_encode)
                byte_encode = data_encode.tobytes()
                image_file_out.write(byte_encode)
    json_file.write("]")
