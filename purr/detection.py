import sys

import torch
import time
# from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
from utils.general import non_max_suppression, xyxy2xywh, check_img_size
# from models.experimental import attempt_load
import glob
import math
import os
import random
from copy import copy
from pathlib import Path

import cv2
# import matplotlib
# import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
# import seaborn as sns
import torch
import torchvision
# import yaml
from PIL import Image, ImageDraw, ImageFont
from models.experimental import attempt_load
from os import PathLike
from typing import Union


# from scipy.signal import butter, filtfilt

# class Ensemble(torch.nn.ModuleList):
#     # Ensemble of models
#     def __init__(self):
#         super(Ensemble, self).__init__()
#
#     def forward(self, x, augment=False):
#         y = []
#         for module in self:
#             y.append(module(x, augment)[0])
#         # y = torch.stack(y).max(0)[0]  # max ensemble
#         # y = torch.stack(y).mean(0)  # mean ensemble
#         y = torch.cat(y, 1)  # nms ensemble
#         return y, None  # inference, train output
#
#
# ##### basic ####
#
# def autopad(k, p=None):  # kernel, padding
#     # Pad to 'same'
#     if p is None:
#         p = k // 2 if isinstance(k, int) else [x // 2 for x in k]  # auto-pad
#     return p
#
#
# class Conv(torch.nn.Module):
#     # Standard convolution
#     def __init__(self, c1, c2, k=1, s=1, p=None, g=1, act=True):  # ch_in, ch_out, kernel, stride, padding, groups
#         super(Conv, self).__init__()
#         self.conv = torch.nn.Conv2d(c1, c2, k, s, autopad(k, p), groups=g, bias=False)
#         self.bn = torch.nn.BatchNorm2d(c2)
#         self.act = torch.nn.SiLU() if act is True else (
#             act if isinstance(act, torch.nn.Module) else torch.nn.Identity())
#
#     def forward(self, x):
#         return self.act(self.bn(self.conv(x)))
#
#     def fuseforward(self, x):
#         return self.act(self.conv(x))


def clip_coords(boxes, img_shape):
    # Clip bounding xyxy bounding boxes to image shape (height, width)
    boxes[:, 0].clamp_(0, img_shape[1])  # x1
    boxes[:, 1].clamp_(0, img_shape[0])  # y1
    boxes[:, 2].clamp_(0, img_shape[1])  # x2
    boxes[:, 3].clamp_(0, img_shape[0])  # y2


def scale_coords(img1_shape: torch.Size, coords: torch.Tensor, img0_shape: torch.Size, ratio_pad=None, centered_pad: bool = True):
    # Rescale coords (xyxy) from img1_shape to img0_shape
    if ratio_pad is None:  # calculate from img0_shape
        gain = min(img1_shape[0] / img0_shape[0], img1_shape[1] / img0_shape[1])  # gain  = old / new
        pad = (img1_shape[1] - img0_shape[1] * gain) / 2, (img1_shape[0] - img0_shape[0] * gain) / 2  # wh padding
    else:
        gain = ratio_pad[0][0]
        pad = ratio_pad[1]

    if centered_pad:
        coords[:, 0] -= pad[0]  # x padding
        coords[:, 2] += pad[0]  # x padding
        coords[:, 1] -= pad[1]  # y padding
        coords[:, 3] -= pad[1]  # y padding
    else:
        coords[:, [0, 2]] -= pad[0]  # x padding
        coords[:, [1, 3]] -= pad[1]  # y padding
    coords[:, :4] /= gain
    clip_coords(coords, img0_shape)
    return coords


# def xyxy2xywh(x):
#     # Convert nx4 boxes from [x1, y1, x2, y2] to [x, y, w, h] where xy1=left-top, xy2=right-bottom
#     y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
#     y[0] = (x[0] + x[2]) / 2  # x center
#     y[1] = (x[1] + x[3]) / 2  # y center
#     y[2] = x[2] - x[0]  # width
#     y[3] = x[3] - x[1]  # height
#     return y

# OpenCV box plotter, obsolete
# def plot_one_box(x, img, color=None, label=None, line_thickness=3):
#     # Plots one bounding box on image img
#     tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
#     color = color or [random.randint(0, 255) for _ in range(3)]
#     c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
#     cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
#     if label:
#         tf = max(tl - 1, 1)  # font thickness
#         t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
#         c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
#         cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
#         cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def plot_one_box(x: list, img: torch.Tensor,
                 color: list[str | tuple[int, int, int]] | str | tuple[int, int, int] | None = None, label: str = None,
                 line_thickness: int = 3) -> torch.Tensor:
    img = torchvision.utils.draw_bounding_boxes(img, boxes=torch.Tensor([x], device='cpu'), labels=[label],
                                                colors=color, width=line_thickness)
    return img


def letterbox(img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32):
    # Resize and pad image while meeting stride-multiple constraints
    shape = img.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)


# def load_model(weights_filename, device_map=None):
#     model = Ensemble()
#     for w in weights if isinstance(weights, list) else [weights]:
#         ckpt = torch.load(w, map_location=device_map)
#         model.append(ckpt['ema' if ckpt.get('ema') else 'model'].float().fuse().eval())
#
#     # Compatibility updates
#     for m in model.modules():
#         if type(m) in [torch.nn.Hardswish, torch.nn.LeakyReLU, torch.nn.ReLU, torch.nn.ReLU6, torch.nn.SiLU]:
#             m.inplace = True  # pytorch 1.7.0 compatibility
#         elif type(m) is torch.nn.Upsample:
#             m.recompute_scale_factor = None  # torch 1.11.0 compatibility
#         elif type(m) is Conv:
#             m._non_persistent_buffers_set = set()  # pytorch 1.6.0 compatibility
#
#     if len(model) == 1:
#         return model[-1]  # return model
#     else:
#         print('Ensemble created with %s\n' % weights)
#         for k in ['names', 'stride']:
#             setattr(model, k, getattr(model[-1], k))
#         return model  # return ensemble


# config variables
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # force torch.cuda.is_available() = False
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
half = device.type != 'cpu'  # half precision only supported on CUDA
save_processed_img = True
save_processed_description = True

# source = #TODO: get image to run on
weights = 'cat-and-ear-model.pt'
model = attempt_load(weights, map_location=device)
stride = int(model.stride.max())  # model stride
imgsz = check_img_size(640, s=stride)  # check img_size
if half:
    model.half()

# inference
if device.type != 'cpu':
    model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once

# initialize img dims
old_img_w = old_img_h = imgsz
old_img_b = 1

# Get names and colors
names = model.module.names if hasattr(model, 'module') else model.names
colors = tuple([[random.randint(0, 255) for _ in range(3)] for _ in names])

t0 = time.time()


def decode_video(video_filepath: Union[str, PathLike]):
    video_reader = torchvision.io.VideoReader(str(video_filepath))
    # video_reader = torchvision.io.read_video(str(video_filepath))
    for frame in video_reader:
        yield frame["data"]

def decode_image(img: torch.Tensor | bytes | bytearray, force_cpu_decode: bool = False) -> torch.Tensor:
    if isinstance(img, bytes):
        img = bytearray(img)
    # img = np.asarray(img)  # not sure if necessary, depends on message payload typing
    # img = cv2.imdecode(img, flags=cv2.IMREAD_COLOR)
    # convert to tensor if not already
    if not isinstance(img, torch.Tensor):
        img = torch.ByteTensor(img, device='cpu')
    img = torchvision.io.decode_jpeg(img, torchvision.io.ImageReadMode.RGB, device=device.type if not force_cpu_decode else 'cpu')
    if force_cpu_decode:
        img = img.to(device)
    return img


def process_image(img, return_original=False) -> (list, torch.Tensor):
    """
    Process Individual Images
    :param return_original: whether to return the original image or the image with labels on it
    :param img: a bytearray like object containing the encoded image
    :returns description, img_processed: returns a tuple containing descriptions: the list of objects, locations, and confidences and the img_processed: the raw image (unencoded) with labels and bounding boxes as a numpy array
    """
    global old_img_w, old_img_h, old_img_b
    img = decode_image(img)
    img_og = img
    # img = letterbox(img, 640, stride=32)[0] Replace with:
    image_colors, height, width = img.shape
    pad_amount = int(abs(height - width) / 2)
    padding_amount = (0, pad_amount) if width > height else (pad_amount, 0)
    img = torchvision.transforms.Pad(padding=padding_amount, fill=114)(img)
    img = torchvision.transforms.Resize((640, 640))(img)
    # img =  # TODO: determine image input paramters, colorspace (BGR vs RGB vs GRAY, etc.), and convert to numpy RGB x Width x Height array, then to "contiguous array"
    # img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    # img = np.ascontiguousarray(img)
    # end simple transfer from todo, may need to be modified based on input
    # img = torch.from_numpy(img).to(device)
    img, pred = run_model_on_image(img)

    img_og, objects_detected = process_model_output(img, img_og, pred, return_original)

    return objects_detected, img_og


def process_model_output(img: torch.Tensor, img_og: torch.Tensor, pred: torch.Tensor, return_original: bool = True) -> (torch.Tensor, list):
    objects_detected = []
    global colors
    for i, det in enumerate(pred):
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img_og.shape[1:], centered_pad=False).round()

            # Write results
            for *xyxy, conf, cls in reversed(det):
                if save_processed_description:  # Write to file
                    objects_detected.append(
                        {"confidence": float(conf), "class": names[int(cls)], "left-top": [int(xyxy[0]), int(xyxy[1])],
                         "right-bottom": [int(xyxy[2]), int(xyxy[3])]})

                if not return_original:  # Add bbox to image
                    label = f'{names[int(cls)]} {conf:.2f}'
                    img_og = plot_one_box(xyxy, img_og, label=label, color=colors[int(cls)], line_thickness=3)
    return img_og, objects_detected


def run_model_on_image(img: torch.Tensor) -> (torch.Tensor, torch.Tensor):
    global old_img_b, old_img_h, old_img_w
    img = img.half() if half else img.float()
    img /= 255.0  # normalize to 0-1 double instead of 0-255 uint8 (possible loss of precision)
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    # Warmup
    if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
        old_img_b = img.shape[0]
        old_img_h = img.shape[2]
        old_img_w = img.shape[3]
        for i in range(3):
            model(img)[0]  # TODO: test augment=
    with torch.no_grad():
        pred = model(img)  # TODO: test with augment=True
        pred = pred[0]
        pred = non_max_suppression(pred, conf_thres=0.5)
    return img, pred
