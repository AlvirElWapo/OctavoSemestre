import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import interactive
interactive(True)

def Colocar_pantalla(nombre_de_pantalla):
    #------ ACOMODAR LA IMAGEN PARA QUE SE VEA COMPLETA EN MI PANTALLA
    #------ SE DEBE AJUSTAR DEPENDIENDO LA IMÁGEN Y EL TAMAÑO DE PANTALLA
    cv2.moveWindow(nombre_de_pantalla, 10,50)

def Crear_Histograma(Imagen, numero):
    plt.hist(Imagen.ravel(), 256, [0,256]);
    plt.savefig('Histogramas/Histograma' + numero + '.png')
    plt.close()

def crear_Histograma_RGB(Imagen, numero):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([Imagen],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.savefig('Histogramas/Histograma' + numero + '.png')
    plt.close()


img = cv2.imread('Imagen4.jpg', 1)
while((cv2.waitKey() & 0xFF) != "q"):
    cv2.imshow('ventana_generica', img)
    Colocar_pantalla('ventana_generica')


#cv2.waitKey(0)
crear_Histograma_RGB(img,"1");
# PRIMER SISTEMA DE COLOR ---> ESCALA DE GRISES

gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
cv2.imshow('ventana_generica', gris);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
Crear_Histograma(gris,"2")

# SEGUNDO SISTEMA DE COLOR ---> XYZ

XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ);
cv2.imshow('ventana_generica', XYZ);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
crear_Histograma_RGB(XYZ,"3")


# TERCER SISTEMA DE COLOR ---> YCrCB

YCRCB = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb);
cv2.imshow('ventana_generica', YCRCB);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
crear_Histograma_RGB(YCRCB,"4")


#CUARTO SISTEMA DE COLOR ---> HLS


HLS = cv2.cvtColor(img, cv2.COLOR_RGB2HLS);
cv2.imshow('ventana_generica', HLS);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);

crear_Histograma_RGB(HLS,"5")

#QUINTO SISTEMA DE COLOR ---> LAB

LAB = cv2.cvtColor(img, cv2.COLOR_RGB2Lab);
cv2.imshow('ventana_generica', LAB);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
crear_Histograma_RGB(LAB,"6")

#SEXTO SISTEMA DE COLOR ---> LUV

LUV = cv2.cvtColor(img, cv2.COLOR_RGB2Luv);
cv2.imshow('ventana_generica', LUV);
Colocar_pantalla('ventana_generica')
cv2.waitKey(0);
crear_Histograma_RGB(LUV,"7")




