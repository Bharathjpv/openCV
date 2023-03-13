# import cv2 as cv

# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(len(flags))

######################### Object Tracking ##############################33
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # convert bgr to hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)


    res = cv.bitwise_and(frame, frame)

    cv.imshow('window',mask)

    k = cv.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cv.destroyAllWindows()