import numpy as np
import cv2 as cv

#################### Image addition ######################
# x = np.uint8([250])
# y = np.uint8([10])

# print(x,y)

# print( cv.add(x,y) )

# print( x+y ) 

#################### Image Blending ######################

# img1 = cv.imread('image.jpg')
# img2 = cv.imread('roi.jpg')

# img1 = cv.resize(img1, (450, 280))

# print(img1.shape, img2.shape)

# dst = cv.addWeighted(img1, 0.5, img2, 0.5, 0)
# cv.imshow('dst', dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

############################ Bit wise operations #####################

img1 = cv.imread('image.jpg')
img2 = cv.imread('OpenCV_Logo.png')

img1 = cv.resize(img1, (450, 280))

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

# cv.imshow('roi', roi)
# Now create a mask of img1 and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

print(ret)
mask_inv = cv.bitwise_not(mask)

# Black out the area of img1 in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# put logo in roi and modefy the image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('window', img1)

cv.waitKey(0)
cv.destroyAllWindows()