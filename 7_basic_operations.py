####################### Accessing and Modefying Pixels ############################

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.imread('image.jpg')



# accessing pixel
# px = img[100, 100]
# print(px)

# # acessing blue pixel
# blue = img[100, 100, 0]
# print(blue)

# # modefy the image pixel value
# img[100,100] = [255,255,255]
# print( img[100,100] )

# print(img[10,10])
# print(img.item(10,10,2))

# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

# print(img.shape)
# print(img.size)
# print(img.dtype)

# cv.imshow('window', img)
# cv.waitKey(0)


############################ IMAGE - ROI ############################

# img = cv.imread('image.jpg')
# birds = img[80:120, 320:550]
# img[120:160, 320:550] = birds

# print(birds.shape)


# splitting and merging image

# b, g, r = cv.split(img)
# print(img.shape)
# print(b.shape,g.shape, r.shape)


# cv.imshow('window', img)
# cv.waitKey(0)


########################### Making Borders ##########################

img = cv.imread('image.jpg')


blue = [255,0,0]

# src, top, bottom, left, right, bordertype

replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=blue)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
