import cv2 as cv
import numpy as np
import sys
import os

net = cv.dnn.readNetFromDarknet(os.path.join('data', 'yolov3-tiny.cfg'), os.path.join('data', 'yolov3-tiny.weights'))
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

layer_names = net.getLayerNames()
output_layer_names = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

IMAGE_WIDTH = 416
IMAGE_HEIGHT = 416

def find_person(img, outputs):
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                if len(sys.argv) > 1 and sys.argv[1] == '--show':
                    box = detection[:4] * np.array([IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    #box = [x, y, int(width), int(height)]
                    cv.rectangle(img, (x, y), (x + width, y + height), (255, 255, 0), 2)
                return True
    return False


def do_frame(img):
    img = img[1000:1960, 1050:2330]
    img = cv.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layer_names)
    result = find_person(img, outputs)
    if len(sys.argv) > 1 and sys.argv[1] == '--show':
        img = cv.resize(img, (0, 0), fx=2, fy=2)
        cv.imshow('window',  img)
        cv.waitKey(1)
    else:
        print(result)


if __name__ == '__main__':
    rtsp_url = os.environ.get('RTSP_URL')
    cap = cv.VideoCapture(rtsp_url)
    while True:
        ret, img = cap.read()
        if not ret:
            break
        try:
            do_frame(img)
        except Exception as e:
            print(e)

    # for img_path in glob.glob('/home/whoever/Pictures/*.jpg'):
    #     try:
    #         do_frame(cv.imread(img_path))
    #     except Exception as e:
    #         print(e)
