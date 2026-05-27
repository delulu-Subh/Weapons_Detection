import numpy as np
import cv2
import imutils
import datetime
import matplotlib.pyplot as plt

# Load XML cascade
gun_cascade = cv2.CascadeClassifier('models/gun_detector.xml')

# Start webcam
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False

while True:
    
    ret, frame = camera.read()

    if not ret:
        break

    # Resize frame
    frame = imutils.resize(frame, width=500)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns
    gun = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=20,
        minSize=(100, 100)
    )

    # If gun detected
    if len(gun) > 0:
        gun_exist = True

    # Draw rectangles
    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Store first frame
    if firstFrame is None:
        firstFrame = gray
        continue

    # Add timestamp
    cv2.putText(
        frame,
        datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
        (10, frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        1
    )

    # Show result
    cv2.imshow("Security Feed", frame)

    # Print if gun detected
    if gun_exist:
        print("Gun detected!")

    # Quit on pressing q
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()