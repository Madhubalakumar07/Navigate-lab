import cv2 as cv
import numpy as np

# read img
img = cv.imread('Datasets/images/sample 6.jpg')
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)

merge = cv.merge([b, g, r])
cv.imshow('Merged Image', merge)

cv.waitKey(0)