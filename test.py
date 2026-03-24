import cv2
import numpy as np


capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = capture.read()
    if not ret:
        print("error mit dem frame")
        break

    cv2.imshow('frame hihi', frame)

    if cv2.waitKey(0):
        break

image = np.zeros((512,512,3), np.uint8)

cv2.line(image, (0, 0), (512,512), (255,0,0), 50)

cv2.imshow('Das ist das bild', image)

cv2.waitKey(0)