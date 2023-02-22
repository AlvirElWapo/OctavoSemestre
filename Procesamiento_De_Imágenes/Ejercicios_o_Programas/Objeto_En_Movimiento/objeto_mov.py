import cv2
import numpy as np

video = cv2.VideoCapture(0)
arra = np.ones(((5),(5)), np.uint8)
rangmax = np.array([50, 255, 50])
rangmin = np.array([0, 51, 0])

while(True):
    ret, frame = video.read()
    mascara = cv2.inRange(frame, rangmin, rangmax)
    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, arra)
    x,y,w,h = cv2.boundingRect(opening)
    cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 4)
    cv2.circle(frame,(x+w//2, y+h//2),6, (0,255,0), -1)
    cv2.imshow('camara', frame)
    q = cv2.waitKey(1) and 0xFF
    if q==27:
        break

cv2.destroyAllWindows()
