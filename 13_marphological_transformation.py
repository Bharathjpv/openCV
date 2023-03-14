import cv2 as cv
import numpy as np

############################### Erosion #######################3333

img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)



cv.imshow('image', img)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)

cv.imshow('erosion', erosion)

dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow('dilation', dilation)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('opening', opening)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('closing', closing)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('gradient', gradient)

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('tophat', tophat)

cv.waitKey(0)
cv.destroyAllWindows()