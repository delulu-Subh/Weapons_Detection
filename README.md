# Weapon Detection Using Python & OpenCV

## Overview

This project is a basic real-time object detection system using:

- OpenCV
- Haar Cascade XML model
- Webcam feed

The system captures live video from a webcam, processes each frame, detects possible weapons using a Haar Cascade classifier, and displays the result in real time.

---

# Project Workflow

```text
Webcam
   ↓
Capture Frame
   ↓
Resize
   ↓
Convert to Grayscale
   ↓
Run Haar Cascade Detection
   ↓
Draw Bounding Boxes
   ↓
Display Output
   ↓
Repeat
```

---

# Libraries Used

## NumPy

```python
import numpy as np
```

NumPy is used for numerical and matrix operations.

OpenCV internally stores images as NumPy arrays.

---

## OpenCV

```python
import cv2
```

Main computer vision library used for:

- Webcam access
- Image processing
- Object detection
- Drawing rectangles
- Displaying video feed

---

## Imutils

```python
import imutils
```

Helper library for OpenCV.

Used mainly for easy image resizing and preprocessing.

---

## Datetime

```python
import datetime
```

Used for displaying current date and time on the webcam feed.

---

## Matplotlib

```python
import matplotlib.pyplot as plt
```

Plotting library.

Currently not required in this project and can be removed safely.

---

# Loading the XML Model

```python
gun_cascade = cv2.CascadeClassifier('models/gun_detector.xml')
```

Loads the Haar Cascade XML classifier.

The XML file contains trained object detection features used to identify weapons.

---

# Starting Webcam

```python
camera = cv2.VideoCapture(0)
```

Opens the default webcam.

- `0` → default camera
- `1`, `2` → external cameras if connected

---

# Variables

## First Frame

```python
firstFrame = None
```

Stores the first grayscale frame.

Usually useful for motion detection.

---

## Detection Flag

```python
gun_exist = False
```

Boolean variable used to track whether a gun has been detected.

---

# Main Detection Loop

```python
while True:
```

Runs continuously to process webcam frames in real time.

---

# Reading Webcam Frames

```python
ret, frame = camera.read()
```

Returns:

- `ret` → whether frame capture was successful
- `frame` → image captured from webcam

---

```python
if not ret:
    break
```

Stops the program if webcam capture fails.

---

# Frame Resizing

```python
frame = imutils.resize(frame, width=500)
```

Resizes frame to width 500.

Benefits:

- Faster processing
- Lower CPU usage

---

# Grayscale Conversion

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

Converts image to grayscale.

Haar Cascade classifiers work only on grayscale images.

Benefits:

- Faster computation
- Simpler processing

---

# Weapon Detection

```python
gun = gun_cascade.detectMultiScale(
```

Main object detection function.

Scans the image at multiple scales and detects possible weapons.

---

# Detection Parameters

## Input Image

```python
gray
```

Grayscale image used for detection.

---

## Scale Factor

```python
scaleFactor=1.3
```

Controls image scaling during detection.

Smaller values:
- More accurate
- Slower

---

## Minimum Neighbors

```python
minNeighbors=20
```

Controls detection strictness.

Higher values:
- Fewer false positives
- Harder detections

---

## Minimum Object Size

```python
minSize=(100, 100)
```

Ignores objects smaller than 100×100 pixels.

---

# Detection Result

```python
if len(gun) > 0:
```

Checks whether any weapons were detected.

---

```python
gun_exist = True
```

Updates detection flag.

---

# Drawing Bounding Boxes

```python
for (x, y, w, h) in gun:
```

Detection coordinates:

- `x` → horizontal position
- `y` → vertical position
- `w` → width
- `h` → height

---

```python
cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
```

Draws rectangle around detected object.

Parameters:

- Image
- Top-left coordinate
- Bottom-right coordinate
- Color `(255, 0, 0)` = Blue
- Thickness = 2

---

# Timestamp Overlay

```python
cv2.putText(
```

Displays current time on the frame.

---

```python
datetime.datetime.now().strftime(...)
```

Gets formatted current date and time.

---

# Displaying Video Feed

```python
cv2.imshow("Security Feed", frame)
```

Displays live webcam feed.

Window title:

```text
Security Feed
```

---

# Detection Alert

```python
if gun_exist:
```

Checks whether weapon is detected.

---

```python
print("Gun detected!")
```

Prints alert message in terminal.

---

# Keyboard Input

```python
key = cv2.waitKey(1) & 0xFF
```

Waits 1 millisecond for key input.

---

```python
if key == ord('q'):
```

Press `q` to quit application.

---

# Cleanup

## Release Webcam

```python
camera.release()
```

Releases webcam resource.

---

## Close Windows

```python
cv2.destroyAllWindows()
```

Closes all OpenCV windows safely.

---

# Project Structure

```text
weapon-detection/
│
├── gun_detection.py
├── requirements.txt
├── README.md
│
├── models/
│   └── gun_detector.xml
│
└── screenshots/
    └── detection_demo.png
```

---

# Limitations

Haar Cascade weapon detection is outdated and can produce inaccurate detections.

Modern object detection systems use:

- YOLOv8
- SSD
- Faster R-CNN
- TensorFlow Object Detection API

These models use deep learning and provide significantly better accuracy.

---

# Run Project

```bash
python gun_detection.py
```
