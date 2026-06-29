import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Datasets/images/sample 6.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(img, img, mask=circle)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
