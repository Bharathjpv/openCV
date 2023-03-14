import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


######################## Canny Edge detection ########################


# img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)

# edges = cv.Canny(img, 100, 240)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

########################## Image Pyramids #############################

img = cv.imread('image.jpg')
print(img.shape)
lower_reso = cv.pyrDown(img)
print(lower_reso.shape)
# cv.imshow('image', lower_reso)

high_reso = cv.pyrUp(lower_reso)
print(high_reso.shape)
cv.waitKey(0)
cv.destroyAllWindows()

