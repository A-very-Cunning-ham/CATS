import glob
import sys
from pathlib import Path
import torch
import torchvision
import platform
from instagram_cat_datasets import InstagramEarDataset
import tqdm

# CONSTANTS
batch_size = 300
device = torch.device(
    "cuda:0" if torch.cuda.is_available() else "cpu")  # Check if GPU is available and use it, otherwise use CPU

try:
    og_data_path = Path(sys.argv[1])
    image_folder = Path(sys.argv[2])
except:
    print("Arguments 1 and 2 must be the path to the model folder and the path to the folder containing images to run models on")
    sys.exit(-1)

# Path hardcoding
# if platform.system() == "Linux":
#     og_data_path = Path("/mnt/e/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/classifier_images")
#     image_folder = Path("/mnt/e/Datasets/CatsEartipped/cleaned_ears_and_faces")
# elif platform.system() == "Windows":
#     og_data_path = Path("E:/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/classifier_images")
#     image_folder = Path("E:/Datasets/CatsEartipped/cleaned_ears_and_faces")
# else:
#     print("You are on another system")
#     sys.exit(-1)

# load model from file
model = torchvision.models.resnet152(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load(og_data_path.joinpath("eartip-classifier.pt"), map_location=device))
model.eval()
model.to(device)
# load required image transform from file
transform = torch.load(og_data_path.joinpath("eartip-classifier-transform.transform"))
# # create a random 3x500x500 tensor
# test_image = torch.rand(3, 500, 500, dtype=torch.float32, device=device)
# # transform the image
# test_image = transform(test_image.unsqueeze(0))
# # test the model with that image
# model(test_image)

if not image_folder.is_dir():
    print(f"{image_folder} is not a directory")
    sys.exit(-1)

ear_images = image_folder.glob("*Cat Ear*.jpg")
dataset = InstagramEarDataset(list(ear_images), transform=transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=0)

# run model on all images in dataset and save images of class 1 with over 90% confidence to a text file
cut_ears = 0  # Initialize the number of cut predictions to zero
total = 0  # Initialize the total number of predictions to zero
cut_ear_image_paths = []
with torch.no_grad():
    for data in tqdm.tqdm(dataloader):  # for data in
        inputs, labels = data  # Get the inputs and labels from the data
        inputs = inputs.to(device)  # Move the inputs to device
        labels = labels.to(device)  # Move he labels to device

        outputs = model(inputs)  # Forward pass: compute the outputs by passing the inputs to the model
        _, predicted = torch.max(outputs.data,
                                 1)  # Get the predicted class labels by taking the maximum output along the dimension 1
        confidence = torch.nn.functional.softmax(outputs.data, dim=1)  # Get the confidence of the prediction
        class_to_care_about = 1
        # add all the image paths and confidences to the list if the prediction is cut without using list comprehension
        cut_ear_image_paths.extend([(str(dataset.img_list[total + i]), confidence[i][class_to_care_about], predicted[i]) for i in range(len(predicted))])
        total += labels.size(0)  # Add the batch size to the total number of predictions
        cut_ears += (
                    predicted == class_to_care_about).sum().item()  # Add the number of cut predictions to the total number of cut predictions

print(f"Cut ears: {cut_ears} | {cut_ears / total:.2%}")
with open("uncut_instagram.txt", "w") as f:
    for image_path, conf, class_predicted in cut_ear_image_paths:
        f.write(f"{image_path}, {conf.squeeze().to('cpu').numpy()}, {class_predicted}\n")
