import cv2 as cv

img = cv.imread('Datasets/images/sample 6.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Image', gray)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print(f'Number of faces detected: {len(faces)}')
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(f'Face detected at: x={x}, y={y}, width={w}, height={h}')
    crop = img[y:y + h, x:x + w]
    cv.imshow('Cropped Face', crop)
cv.imshow('faces', img)
cv.waitKey(0)