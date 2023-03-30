import re
import requests

num_classes = 1
height = 416
width = 416
max_batch = num_classes * 2000
step1 = 0.8 * max_batch
step2 = 0.9 * max_batch
num_filters = (num_classes + 5) * 3
batch = 64
subdivisions = 4

file_path = 'data/yolov3-tiny.cfg'
file_url = 'https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg'

response = requests.get(file_url, allow_redirects=True)
open(file_path, 'wb').write(response.content)

with open(file_path, 'r') as f:
    s = f.read()
s = re.sub('max_batches = \d*', f'max_batches={max_batch}', s)
s = re.sub('steps=\d*,\d*', f'steps={step1:.0f},{step2:.0f}', s)
s = re.sub('classes=\d*', f'classes={num_classes}', s)
s = re.sub('pad=1\nfilters=\d*', f'pad=1\nfilters={num_filters:.0f}', s)
s = re.sub('batch=\d*', f'batch={batch}', s)
s = re.sub('subdivisions=\d*', f'subdivisions={subdivisions}', s)
s = re.sub('height=\d*', f'height={height}', s)
s = re.sub('width=\d*', f'width={width}', s)
with open(file_path, 'w') as f:
    f.write(s)
