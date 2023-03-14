import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

######################### Scaling #########################

# import numpy as np
# import cv2 as cv

# img = cv.imread('image.jpg')

# print(img.size, img.shape)


# res = cv.resize(img, None, fx=2, fy=2, interpolation= cv.INTER_CUBIC)
# cv.imshow('window', img)
# print(res.size, res.shape)
# cv.imshow('window1', res)

# cv.waitKey(0)
# cv.destroyAllWindows()

############################# Translation #########################

# import numpy as np
# import cv2 as cv

# img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)

# rows, cols = img.shape
# print (rows, cols)

# M = np.float32([[1,0,100],[0,1,100]])
# print(M)

# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow('window', img)
# cv.imshow('window1', dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

######################## Rotation #####################

# import cv2 as cv

# img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)

# rows, cols = img.shape
# print(rows, cols)

# M = cv.getRotationMatrix2D(((cols-1)/2., (rows-1)/2.), 45,1)
# print(M)

# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow('window', img)
# cv.imshow('window1', dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

####################### Affine Transformation ###################3



# img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)

# rows, cols = img.shape

# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# print(pts1)
# M = cv.getAffineTransform(pts1,pts2)
# print(M)

# dst = cv.warpAffine(img, M, (cols, rows))

# # cv.imshow('window', img)
# # cv.imshow('window1', dst)
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()

######################### Prespective transforamtion ##########################33333

img = cv.imread('sudoku.jpeg', cv.IMREAD_GRAYSCALE)
rows, cols = img.shape

pts1 = np.float32([[40, 80],[125, 45],[80, 170],[170, 125]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])

M = cv.getPerspectiveTransform(pts1,pts2)
res = cv.warpPerspective(img,M,(200,200))
print(M)

cv.imshow('window', img)
# cv.imshow('window1', dst)
cv.imshow('window2', res)
cv.imwrite('sudoku_trans.png', res)

cv.waitKey(0)
cv.destroyAllWindows()