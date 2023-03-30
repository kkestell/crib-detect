# YOLOv3 Fine Tuning

Fine tune a YOLOv3 model to detect a specific object.

## Training

```console
$ source venv/bin/activate
```

Copy training images into the label tool's `Images` directory:

```console
$ ./copy-images.sh
```

Label all of your training images.

```console
$ python label-tool/main.py
```

Copy the images and labels into the `data` directory, transforming the labels into YOLO format:

```console
$ ./assemble-training-data.sh
```

Create a YOLO model configuration file:

```console
$ ./make-model-config.sh
```

Upload the `data` directory to Google Drive and name it `yolo-data`.

Then, upload `yolov3-fine-tuning.ipynb` to Google Colab and run it.

When training is complete, download `yolov3-tiny_best.weights` from Google Drive and copy it into the `data` directory in this repository.


## Running

```console
$ python main.py --show RTSP_URL=rtsp://user:pass@ip:port/
```
