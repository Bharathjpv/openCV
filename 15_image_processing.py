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

# img = cv.imread('image.jpg')

# print(img.shape)
# lower_reso = cv.pyrDown(img)
# print(lower_reso.shape)


# high_reso = cv.pyrUp(lower_reso)
# print(high_reso.shape)

# cv.imshow('image', high_reso)

# laplacian = cv.Laplacian(img, cv.CV_64F)
# lower_res_lap = cv.pyrDown(laplacian)

# cv.imshow('lap', laplacian)
# cv.imshow('lap_down', lower_res_lap)

# cv.waitKey(0)
# cv.destroyAllWindows()

############################# Image blending using pyramids #####################


A = cv.imread('apple.jpg')
B = cv.imread('orange.jpeg')
rows, cols = A.shape[:2]
A = cv.resize(A, (cols, cols))
B = cv.resize(B, (cols, cols))
# cv.imshow('apple', A)
# cv.imshow('orange', B)
print(A.shape, B.shape)

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
    

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)
    

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    size = (gpA[i-1].shape[1], gpA[i-1].shape[0])
    GE = cv.pyrUp(gpA[i], dstsize=size)
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    size = (gpB[i-1].shape[1], gpB[i-1].shape[0])
    GE = cv.pyrUp(gpB[i], dstsize=size)
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
cv.imshow('Pyramid_blending2',ls_)
cv.imshow('Direct_blending',real)

cv.waitKey(0)
cv.destroyAllWindows()

