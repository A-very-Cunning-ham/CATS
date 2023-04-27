import json
import sys
from pathlib import Path
import torchvision.utils
import numpy as np
import torch

db_json_filepath = sys.argv[1]
images_folder = Path(sys.argv[2])
with open(db_json_filepath, 'r') as db_json_file:
    db_json = json.load(db_json_file)

colors = {"Cat Ear": (255, 0, 0), "Cat Face": (0, 255, 0)}
for item in db_json:
    image_path = images_folder.joinpath(item['filename'])
    image_tensor = torchvision.io.read_image(str(image_path))
    bounding_boxes = [[od["left-top"][0], od["left-top"][1], od["right-bottom"][0], od["right-bottom"][1]] for od in item['objects-found']]
    bounding_boxes = torch.as_tensor(bounding_boxes, dtype=torch.int32)
    colors_chosen = [colors[od["class"]] for od in item['objects-found']]
    out_image = torchvision.utils.draw_bounding_boxes(image_tensor, bounding_boxes, colors=colors_chosen, labels=[od["class"] for od in item['objects-found']])
    torchvision.io.write_jpeg(out_image, str(image_path))
