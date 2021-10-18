import cv2
import os
 
#RTSP_URL = 'rtsp://user:pass@192.168.0.189:554/h264Preview_01_main'
RTSP_URL = cv2.VideoCapture('rtsp://user1:User123456@192.168.0.238:554/cam/realmonitor?channel=1&subtype=0')


while True:
    _, frame = RTSP_URL.read()
    cv2.imshow('RTSP stream', frame)
    k = cv2.waitKey(1)
 
    if k == ord('q'):
        break
 
RTSP_URL.release()
cv2.destroyAllWindows()
