import cv2 as cv

#read img
img = cv.imread('Datasets/images/sample 6.jpg')
cv.imshow('Original Image', img)

# average blur
avg = cv.blur(img, (7, 7))
cv.imshow('Average Blurred Image', avg)

# gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blurred Image', gauss)

# median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blurred Image', median)

# bilateral blur
bilateral = cv.bilateralFilter(img, 15, 45, 35)
cv.imshow('Bilateral Blurred Image', bilateral)

cv.waitKey(0)