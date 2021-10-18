import cv2
import os
 
RTSP_URL = cv2.VideoCapture('rtsp://username:Users password@ip address:port/streaming/channels<id>')


while True:
    _, frame = RTSP_URL.read()
    cv2.imshow('RTSP stream', frame)
    k = cv2.waitKey(1)
 
    if k == ord('q'):
        break
 
RTSP_URL.release()
cv2.destroyAllWindows()
