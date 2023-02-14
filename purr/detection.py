import torch
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
from models.experimental import attempt_load

source = #TODO: get image to run on
model_path = "./yolov7-custom-repeat/"
weights = model_path + "weitghts/init.pt"
device = select_device("cpu")
model = attempt_load(weights, map_location=device)
stride = int(model.stride.max())  # model stride
imgsz = "640"