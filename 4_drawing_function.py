# cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText()

import numpy as np
import cv2 as cv
import sys

img = np.zeros((512, 512, 3), np.uint8)

# adding line
cv.line(img, (0,0), (511,511), (0, 0, 255), 5)

# adding reactangle
cv.rectangle(img, (350, 0), (510, 152), (0,255,0), 5)

# adding circle
cv.circle(img,(430,76), 76, (0,0,255), -1)

# adding polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# adding text
font = cv.FONT_HERSHEY_SIMPLEX
# image, text, position, font, font_scale, color, size, line_type
cv.putText(img, 'Bharath', (1, 500), font, 4, (255,255,255), 2, cv.LINE_AA)

if img is None:
    sys.exit("Could not read the image.")
cv.imshow('window', img)
cv.waitKey(0)

