import cv2 as cv
import numpy as np

# read the image
img = cv.imread('Datasets/images/sample 6.jpg')
cv.imshow('Original', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.rectangle(blank, (50, 50), (350, 300), 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)