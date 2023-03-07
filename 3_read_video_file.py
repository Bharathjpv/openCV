import numpy as np
import cv2 as cv

cap = cv.VideoCapture('race.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print('stream ended')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()