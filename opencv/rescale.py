import cv2 as cv

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

vid = cv.VideoCapture('Datasets/videos/sample 1.mp4')
while True:
    isTrue, frame = vid.read()
    frame_resized = rescale(frame)
    cv.imshow('Video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
vid.release()
cv.destroyAllWindows()