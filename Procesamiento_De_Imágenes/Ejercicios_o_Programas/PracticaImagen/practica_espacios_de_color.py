import cv2
import numpy as np
from matplotlib import pyplot as plt

def Colocar_pantalla(nombre_de_pantalla):
    #------ ACOMODAR LA IMAGEN PARA QUE SE VEA COMPLETA EN MI PANTALLA
    #------ SE DEBE AJUSTAR DEPENDIENDO LA IMÁGEN Y EL TAMAÑO DE PANTALLA
    cv2.moveWindow(nombre_de_pantalla, 10,50)

def Generar_Histograma(imagen, canales, color):
    hist = cv2.calcHist([imagen], canales, None, [256], [0, 256])
    plt.plot(hist, color=color);
    plt.xlim([0, 256])


img = cv2.imread('Imagen3.png', 1)
cv2.imshow('ventana_generica', img)
Colocar_pantalla('ventana_generica')
Generar_Histograma(img,)
cv2.waitKey(0)


# PRIMER SISTEMA DE COLOR ---> ESCALA DE GRISES

gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
cv2.imshow('ventana_generica', gris);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);


# SEGUNDO SISTEMA DE COLOR ---> XYZ

XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ);
cv2.imshow('ventana_generica', XYZ);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);


# TERCER SISTEMA DE COLOR ---> YCrCB

YCRCB = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb);
cv2.imshow('ventana_generica', YCRCB);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
