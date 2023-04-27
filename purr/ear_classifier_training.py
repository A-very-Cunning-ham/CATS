# Import the necessary modules
import torch
import torchvision
from torchvision.models import ResNet18_Weights, ResNet152_Weights
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import os
from tqdm import tqdm

# set working directory, if necessary
# os.chdir(r'/mnt/e/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/classifier_images')

# Define the hyperparameters
batch_size = 32  # The number of images in each batch
num_epochs = 10  # The number of times to train on the whole dataset
learning_rate = 0.01  # The learning rate for the optimizer
num_classes = 2  # The number of classes (binary)

# Define the transformations for the images
transform = transforms.Compose([
    transforms.Resize(224),  # Resize the images to 256x256 pixels
    transforms.CenterCrop(224),  # Crop the images to 224x224 pixels from the center
    # transforms.RandomRotation(degrees=180),  # Rotate the images by 15 degrees
    transforms.RandomHorizontalFlip(p=0.5),  # Horizontally flip the images with probability 0.5
    transforms.ToTensor(),  # Convert the images to tensors
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    # Normalize the images with mean and standard deviation of ImageNet dataset
])

# Load the training and validation datasets
trainset = torchvision.datasets.ImageFolder(root='train',
                                            transform=transform)  # Load the images from the train folder and apply the transformation
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True,
                                          num_workers=2)  # Create a data loader for the training set


valset = torchvision.datasets.ImageFolder(root='val',
                                          transform=transform)  # Load the images from the val folder and apply the transformation
valloader = torch.utils.data.DataLoader(valset, batch_size=batch_size, shuffle=False,
                                        num_workers=2)  # Create a data loader for the validation set
testset = torchvision.datasets.ImageFolder(root='test',
                                          transform=transform)  # Load the images from the test folder and apply the transformation
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False,
                                        num_workers=2)  # Create a data loader for the test set

# Define the model architecture
model = torchvision.models.resnet152(weights=ResNet152_Weights.DEFAULT)  # Load a pretrained ResNet-18 model from torchvision
model.fc = nn.Linear(model.fc.in_features,
                     num_classes)  # Replace the last fully connected layer with a new one with num_classes outputs

# Move the model to the device (CPU or GPU)
device = torch.device(
    "cuda:0" if torch.cuda.is_available() else "cpu")  # Check if GPU is available and use it, otherwise use CPU
model.to(device)  # Move the model to the device

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss()  # Use cross entropy loss for classification
optimizer = optim.SGD(model.parameters(), lr=learning_rate,
                      momentum=0.9)  # Use stochastic gradient descent with momentum as the optimizer

# Train the model
for epoch in tqdm(range(num_epochs), position=0, leave=False, unit="epoch", colour="green"):  # Loop over the epochs

    running_loss = 0.0  # Initialize the running loss to zero
    for i, data in tqdm(enumerate(trainloader, 0), position=1, leave=False, unit="batch", colour="blue", total=len(trainloader)):  # Loop over the batches of data in the trainloader
        inputs, labels = data  # Get the inputs and labels from the data
        inputs = inputs.to(device)  # Move the inputs to the device
        labels = labels.to(device)  # Move the labels to the device

        optimizer.zero_grad()  # Zero the parameter gradients

        outputs = model(inputs)  # Forward pass: compute the outputs by passing the inputs to the model
        loss = criterion(outputs, labels)  # Compute the loss using the outputs and labels
        loss.backward()  # Backward pass: compute the gradients of the loss with respect to the model parameters
        optimizer.step()  # Update the model parameters using the gradients and optimizer

        running_loss += loss.item()  # Add the loss to the running loss
        if i % 200 == 199:  # Print every 200 batches
            print('[%d, %5d] loss: %.3f' % (
            epoch + 1, i + 1, running_loss / 200))  # Print the epoch, batch and average loss
            running_loss = 0.0  # Reset the running loss to zero

print('Finished Training')  # Print when finished training

# Evaluate the model on the validation set
correct = 0  # Initialize the number of correct predictions to zero
total = 0  # Initialize the total number of predictions to zero
with torch.no_grad():  # Disable gradient computation
    for data in valloader:  # Loop over the batches of data in the valloader
        inputs, labels = data  # Get the inputs and labels from the data
        inputs = inputs.to(device)  # Move the inputs to device
        labels = labels.to(device)  # Move he labels to device

        outputs = model(inputs)  # Forward pass: compute the outputs by passing the inputs to the model
        _, predicted = torch.max(outputs.data,
                                 1)  # Get the predicted class labels by taking the maximum output along the dimension 1
        total += labels.size(0)  # Add the batch size to the total number of predictions
        correct += (
                predicted == labels).sum().item()  # Add the number of correct predictions to the correct number of predictions

# Evaluate the model on the test set
correct = 0  # Initialize the number of correct predictions to zero
total = 0  # Initialize the total number of predictions to zero
with torch.no_grad():  # Disable gradient computation
    for data in testloader:  # Loop over the batches of data in the testloader
        inputs, labels = data  # Get the inputs and labels from the data
        inputs = inputs.to(device)  # Move the inputs to device
        labels = labels.to(device)  # Move he labels to device

        outputs = model(inputs)  # Forward pass: compute the outputs by passing the inputs to the model
        _, predicted = torch.max(outputs.data,
                                 1)  # Get the predicted class labels by taking the maximum output along the dimension 1
        #compute the confidence of the prediction
        confidence = torch.nn.functional.softmax(outputs.data, dim=1)
        total += labels.size(0)  # Add the batch size to the total number of predictions
        correct += (
                predicted == labels).sum().item()  # Add the number of correct predictions to the correct number of predictions

print('Accuracy of the network on the validation images: %d %%' % (
        100 * correct / total))  # Print the accuracy of the network on the validation images

# save it
torch.save(model.state_dict(), 'eartip-classifier.pt')
# save pytorch transforms to a file
torch.save(transform, 'eartip-classifier-transform.transform')