import cv2
import numpy as np

video = cv2.VideoCapture(0)
def figColor(imagenHSV):
    #azul
    azulAlto = np.array([125,255,255],np.uint8)
    azulBajo =np.array([100,100,20],np.uint8)
    rojoBajo1 = np.array([0, 100, 20], np.uint8)
    rojoAlto1 = np.array([10, 255, 255], np.uint8)
    rojoBajo2 = np.array([175, 100, 20], np.uint8)
    rojoAlto2 = np.array([180, 255, 255], np.uint8)
    naranjaBajo = np.array([11, 100, 20], np.uint8)
    naranjaAlto = np.array([19, 255, 255], np.uint8)
    amarilloBajo = np.array([20, 100, 20], np.uint8)
    amarilloAlto = np.array([45, 255, 255], np.uint8)

	#Verde
    verdeBajo = np.array([36, 100, 20], np.uint8)
    verdeAlto = np.array([70, 255, 255], np.uint8)

	#Violeta
    violetaBajo = np.array([130, 100, 20], np.uint8)
    violetaAlto = np.array([145, 255, 255], np.uint8)


	#Rosa
    rosaBajo = np.array([146, 100, 20], np.uint8)
    rosaAlto = np.array([170, 255, 255], np.uint8)

	# Se buscan los colores en la imagen, segun los límites altos
	# y bajos dados
    maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
    maskRojo = cv2.add(maskRojo1, maskRojo2)
    maskNaranja = cv2.inRange(imagenHSV, naranjaBajo, naranjaAlto)
    maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
    maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
    maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
    maskRosa = cv2.inRange(imagenHSV, rosaBajo, rosaAlto)
    maskAzul = cv2.inRange(imagenHSV, azulBajo, azulAlto)
    cntsRojo,_ = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsNaranja,_ = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsAmarillo,_ = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsVerde,_ = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsVioleta,_ = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsRosa,_ = cv2.findContours(maskRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Reemplaza por 1, si tienes OpenCV3
    cntsAzul,_ = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cntsRojo)>0: return 'Rojo'
    elif len(cntsNaranja)>0: return'Naranja'
    elif len(cntsAmarillo)>0: return 'Amarillo'
    elif len(cntsVerde)>0: return'Verde'
    elif len(cntsVioleta)>0: return 'Violeta'
    elif len(cntsRosa)>0: return 'Rosa'
    elif len(cntsAzul)>0:     return'azul'
    return 'None'


def getContours(img,image_hsv):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(frame,cnt,-1,(255,0,0),3)
            perimetro = cv2.arcLength(cnt,True)
            #buscar bordes
            aprrox = cv2.approxPolyDP(cnt,0.02*perimetro,True)
            objCorner = len(aprrox)
            x,y,w,h = cv2.boundingRect(aprrox)
            img_aux = np.zeros(frame.shape[:2], dtype='uint8')
            img_aux = cv2.drawContours(img_aux, [cnt], -1, 255, -1)
            mask_hsv = cv2.bitwise_and(image_hsv, image_hsv, mask=img_aux)
            if objCorner ==3:
                namefig='Triangulo'
            elif objCorner ==4:
                aspecto = w/float(h)
                if aspecto >0.95 and aspecto<1.05:
                    namefig='Cuadrado'
                else:
                    namefig='Rectangulo'
            elif objCorner ==5:
                namefig='Pentagono'
            elif objCorner ==6:
                namefig='Hexagono'
            elif objCorner >10:
                namefig='Circulo'
            else:
                namefig='Circulo'
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,namefig+' '+figColor(mask_hsv),(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)


while True:
    ret,frame = video.read()
    if ret:
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray,(7,7),1)
     imgcanny = cv2.Canny(blur,50,50)
     image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     getContours(imgcanny,image_hsv)
     cv2.imshow("Figuras Geometricas",frame)
     if cv2.waitKey(1) == ord('q'):
        break
