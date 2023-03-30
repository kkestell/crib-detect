import os
import cv2 as cv
import random
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))
training_data_dir = os.path.join(script_dir, 'data', 'training-data')
label_tool_dir = os.path.join(script_dir, 'label-tool')
labels_dir = os.path.join(os.path.join(label_tool_dir, 'Labels'), '001')
images_dir = os.path.join(os.path.join(label_tool_dir, 'Images'), '001')

os.makedirs(training_data_dir, exist_ok=True)

for file in os.listdir(images_dir):
    if not file.endswith('.jpg'):
        continue
    img = cv.imread(os.path.join(images_dir, file))
    label_file = os.path.join(labels_dir, f'{file[:-4]}.txt')
    if not os.path.exists(label_file):
        continue
    with open(label_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    if len(lines) < 2:
        continue
    x1, y1, x2, y2 = [int(line) for line in lines[1].split(' ')]
    x1, y1, x2, y2 = x1/416, y1/416, x2/416, y2/416
    x, y, w, h = (x1+x2)/2, (y1+y2)/2, x2-x1, y2-y1
    out_txt_file = os.path.join(training_data_dir, f'{file[:-4]}.txt')
    out_img_file = os.path.join(training_data_dir, file)
    with open(out_txt_file, 'w') as f:
        f.write(f'0 {x} {y} {w} {h}')
    shutil.copy(os.path.join(images_dir, file), out_img_file)

train_file = os.path.join(script_dir, 'data', 'train.txt')
test_file = os.path.join(script_dir, 'data', 'test.txt')

with open(train_file, 'w') as f:
    pass
with open(test_file, 'w') as f:
    pass

for file in os.listdir(training_data_dir):
    if not file.endswith('.jpg'):
        continue     
    
    if random.random() < 0.9:
        with open(train_file, 'a') as f:
            f.write(f'/content/data/training-data/{file}\n')
    else:
        with open(test_file, 'a') as f:
            f.write(f'/content/data/training-data/{file}\n')
