# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
import sys
import os
import platform
import numpy as np

# Define a list of image paths
with open("uncut_instagram.txt", "r") as f:
    images = f.read().splitlines()
    # split the lines into image path, confidence, and class
    images = [image.split(", ") for image in images if image[-1] == '0']


def windows_to_wsl_filepath(filepath):
    # convert a windows filepath to a wsl filepath
    filepath = f"/mnt/{filepath[0].lower()}{filepath[2:]}".replace("\\", "/")
    return filepath


# Creating a class for the widget
class ImageWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        # Setting the window title and size
        self.setWindowTitle("Image Display")
        self.resize(800, 600)
        # Creating a label for the image
        self.image_label = QLabel()
        # autoscale the image
        self.image_label.setScaledContents(True)
        # Creating a label for the confidence and class
        self.info_label = QLabel()
        # Creating a layout to arrange the labels
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.info_label)
        # Setting the layout to the widget
        self.setLayout(self.layout)
        # Storing the data as an attribute
        self.data = data
        # Initializing the index of the current image
        self.index = 0
        # Creating a timer to update the image every 200 ms
        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_image)
        # Starting the timer
        self.timer.start()
        # Displaying the first image
        self.display_image()

    def display_image(self):
        # Getting the image file path, confidence and class from the data list
        image_file, confidence, class_num = self.data[self.index]
        if platform.system() == "Linux":
            # Converting the image file path to a WSL filepath
            image_file = windows_to_wsl_filepath(image_file)
        if not os.path.exists(image_file):
            raise FileNotFoundError(f"File {image_file} does not exist")
        # Loading the image from the file path
        image = QPixmap(image_file)
        # Setting the image to the image label
        self.image_label.setPixmap(image)
        # # Resizing the image label to fit the image
        # self.image_label.resize(image.width(), image.height())
        # # Resizing the widget to fit the layout
        # self.resize(self.layout.sizeHint())
        # Setting the confidence and class to the info label
        self.info_label.setText(f"Confidence: {confidence}\nClass: {class_num}")

    def update_image(self):
        # Incrementing the index by one
        self.index += 1
        # Wrapping around if the index exceeds the length of the data list
        if self.index >= len(self.data):
            self.index = 0
        # Displaying the image at the new index
        self.display_image()

    def keyPressEvent(self, event):
        # Handling key press events
        if event.key() == Qt.Key_1:
            # If 1 is pressed, move back one image
            self.index -= 1
            # Wrapping around if the index is negative
            if self.index < 0:
                self.index = len(self.data) - 1
            # Displaying the image at the new index
            self.display_image()
        elif event.key() == Qt.Key_2:
            # If 2 is pressed, move back to the first image
            self.index = 0
            # Displaying the image at the new index
            self.display_image()


# Creating an application instance
app = QApplication(sys.argv)
# Creating a widget instance with the data list
widget = ImageWidget(images)
# Showing the widget
widget.show()
# Running the application loop
sys.exit(app.exec_())
