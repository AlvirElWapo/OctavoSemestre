import cv2
import numpy as np

video = cv2.VideoCapture(0)

k = np.ones((5,5), np.ubyte)

while (True):
    ret,frame = video.read()
    rangmax = np.array([50,255,50])
    rangmin = np.array([0,51,0])

    mascara = cv2.inRange(frame,rangmin,rangmax)

    opening = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,k)

    x,y,h,w = cv2.boundingRect(opening)

    cv2.rectangle(frame,(x,y),(x+w, y+h),[0,255,0],4)

    cv2.circle(frame, (x+w//2,y+h//2),6,[0,0,100],-1)

    cv2.imshow('camara',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()