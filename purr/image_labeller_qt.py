# Importing the modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from glob import glob
# Importing the platform module
import platform

# Getting the system name
system = platform.system()
if len(sys.argv):
    print("no folder specified")
    sys.exit(-1)

# Creating a class for the main window
class ImageWindow(QWidget):
    def __init__(self, image_list):
        super().__init__()
        self.image_label = None
        self.quit_button = None
        self.image_list = image_list  # A list of image paths
        self.index = 0  # The current index of the image list
        self.result = {}  # A dictionary to store the results
        self.initUI()  # Initializing the user interface

    def initUI(self):
        # Setting the window title and size
        self.setWindowTitle('Image Classifier')
        self.resize(800, 600)

        # Creating a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(
            self.resize_pixmap(self.image_list[self.index]))  # Resize the pixmap to fit the window

        # Creating a button to quit the program
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.exit_safely)

        # Setting the layout of the widgets
        self.image_label.setGeometry(0, 0, 800, 500)
        self.quit_button.setGeometry(350, 550, 100, 40)

        # Showing the window
        self.show()

    def keyPressEvent(self, event):
        # Handling the key press events
        if event.key() == Qt.Key_1:
            # If 1 is pressed, store the image as uncut and go to the next image
            self.result[self.image_list[self.index]] = 'uncut'
            self.next_image()
        elif event.key() == Qt.Key_2:
            # If 2 is pressed, store the image as cut and go to the next image
            self.result[self.image_list[self.index]] = 'cut'
            self.next_image()
        elif event.key() == Qt.Key_3:
            # If left arrow is pressed, go back to the previous image
            self.prev_image()

    def next_image(self):
        # Going to the next image in the list
        self.index += 1
        if self.index < len(self.image_list):
            # If there are more images, update the label with the new image and resize it to fit the window
            self.image_label.setPixmap(self.resize_pixmap(self.image_list[self.index]))
        else:
            # If there are no more images, write the results to a file and quit
            self.write_results()
            self.quit()

    def prev_image(self):
        # Going to the previous image in the list
        if self.index > 0:
            # If there is a previous image, update the label with it and resize it to fit the window
            self.index -= 1
            self.image_label.setPixmap(self.resize_pixmap(self.image_list[self.index]))

    def write_results(self):
        # Writing the results to a file
        with open('results-cut.txt', 'w') as f:
            for image, label in self.result.items():
                f.write(f'{image}: {label}\n')

    def exit_safely(self):
        # Exiting the program safely
        self.write_results()
        self.quit()

    def quit(self):
        # Quitting the program
        sys.exit()

    def resize_pixmap(self, path):
        # Resizing a pixmap to fit the window without changing aspect ratio
        pixmap = QPixmap(path)  # Load the pixmap from path
        width = pixmap.width()  # Get the original width of pixmap
        height = pixmap.height()  # Get the original height of pixmap
        ratio = width / height  # Get the original aspect ratio of pixmap

        max_width = 800  # The maximum width of window
        max_height = 500  # The maximum height of window

        if ratio > max_width / max_height:
            # Scale by width
            width = max_width
            height = int(width / ratio)
        else:
            # Scale by height
            height = max_height
            width = int(height * ratio)

        pixmap = pixmap.scaled(width, height)  # Scale pixmap with new dimensions

        return pixmap


# Creating a list of sample image paths contained on each line of a text file
image_list = []
with open('results.txt') as f:
    for line in f:
        imagepath, cut_status = line.split(":")
        if cut_status.strip() == 'cut':
            image_list.append(imagepath.strip())

print(image_list)

# for each image in the list, glob every image beginning with the same first 27 characters and "-Cat Ear", add these to a new list
ear_images = []
for image in image_list:
    image_filename_folder, image_filename_file = image.rsplit('/', 1)
    # check if running on windows or linux
    # Checking if the system is windows or linux
    # if system == 'Windows':
    #     # if running on windows
    #     image_filename_folder = "E:/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/"
    # elif system == 'Linux':
    #     # if running on linux
    #     image_filename_folder = "/mnt/e/Datasets/CatsAdrianVideos/cleaned_trail_cam_footage/"
    # else:
    #     print('You are on another system')
    #     sys.exit(-1)

    ear_glob = f"{sys.argv[1]}{image_filename_file[:21]}*Cat Ear*"
    print(ear_glob)
    ear_images.extend(glob(ear_glob))

print(ear_images)
# Creating an application object and an instance of the main window class
app = QApplication(sys.argv)
window = ImageWindow(ear_images)

# Executing the application
sys.exit(app.exec_())
