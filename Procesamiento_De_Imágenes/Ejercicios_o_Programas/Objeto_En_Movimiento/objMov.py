import cv2
import numpy as np


# Loop principal
video = cv2.VideoCapture(0)

# Variable para almacenar una matriz de unos  camara contra lo que se va a comparar
#
k = np.ones((5, 5), np.uint8)


while (True):
    # Obtencion de inforamación en el frame
    ret, frame = video.read()
    #Rango de color
    rangMax= np.array([60,255,150])
    rangMin= np.array([0,51,0])
    
    
    
    #Creacion de una mascara para el color 
    mascara=cv2.inRange(frame,rangMin,rangMax)
    
    #Morfologia, ocupa la mascara y posteriormente la matriz de unos 1s
    #Empalmar la matriz
    #apertura con la matriz de 1s  
                               #Fuente #Tipo de operacion #Respecto a que MAtriz
                               #Kernel
    opening = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,k)
    #Con opening va a saber si se está moviendo 
    x,y,w,h= cv2.boundingRect(opening)
    #La posicion se obtiene de la morfologia
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
    cv2.circle(frame,(x+w//2,y+h//2),6,(0,0,100),1)

    cv2.imshow('camara',frame)    
    cv2.imshow('mascara',mascara)    
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
            break

video.release()
cv2.destroyAllWindows()