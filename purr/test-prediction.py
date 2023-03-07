import detection
import cv2
import utils
import models

with open('cat_01.jpg', 'rb') as image_file:
    buff = image_file.read()
    desc, image = detection.process_image(buff)
    # image = image[0][::-1, :, :].transpose(1, 2, 0)
    cv2.imwrite('cat_processed.jpg', image)
