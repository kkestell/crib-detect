from glob import glob
import cv2 as cv
import os
import random

script_dir = os.path.dirname(os.path.realpath(__file__))
label_tool_dir = os.path.join(script_dir, 'label-tool')
images_dir = os.path.join(os.path.join(label_tool_dir, 'Images'), '001')
source_dir = '/home/kyle/Pictures/Timelapse/Nursery/frames'

fidx = 0
for directory in glob(os.path.join(source_dir, '*')):
    images = glob(os.path.join(directory, '*.jpg'))
    random.shuffle(images)
    images = images[:5]
    for image in images:
        img = cv.imread(image)
        img = img[1000:2000, 1200:2200]
        img = cv.resize(img, (416, 416))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.equalizeHist(img)
        img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        os.makedirs(images_dir, exist_ok=True)
        cv.imwrite(f'{images_dir}/{fidx:03d}.jpg', img)
        fidx += 1
