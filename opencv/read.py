import cv2 as cv

# img = cv.imread('Datasets/images/sample 7.jpg')
# cv.imshow('max', img)

# cv.waitKey(0)

vid = cv.VideoCapture('Datasets/videos/sample 1.mp4')
while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
cv.release()
cv.destroyAllWindows()