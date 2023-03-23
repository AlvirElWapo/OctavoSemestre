import funcs
import cv2
video = cv2.VideoCapture(0)
##Mostrar Normal
while(True):

    ret,frame = video.read()
    if ret == True:
        funcs.hacer_caricatura(frame)
        cv2.imshow('frame',frame)
        funcs.calc_hist(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

##Mostrar Invertido Espejo
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.hacer_espejo(frame))
        funcs.calc_hist(funcs.hacer_espejo(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Mostrar Caricatura
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.hacer_caricatura(frame))
        funcs.calc_hist(funcs.hacer_caricatura(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Mostrar GREEN

while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.ver_hulk(frame))
        funcs.calc_hist(funcs.ver_hulk(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Mostrar GREEN_CARICATURA
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.ver_hulk(funcs.hacer_caricatura(frame)))
        funcs.calc_hist(funcs.ver_hulk(funcs.hacer_caricatura(frame)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
## Umbral
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.hacer_thresh(frame))
        funcs.calc_hist_thresh(funcs.hacer_thresh(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Mascara Green
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.aplicar_mascara(funcs.ver_hulk(frame)))
        funcs.calc_hist(funcs.aplicar_mascara(funcs.ver_hulk(frame)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Espejo pinta RED todos los elementos de ese tipo
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.pintar_red(funcs.hacer_espejo(frame)))
        funcs.calc_hist(funcs.pintar_red(funcs.hacer_espejo(frame)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## Agregar filtro SEPIA
while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.sepia(frame))
        funcs.calc_hist(funcs.sepia(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

## GRABCUT (se traba rete feo)

while(True):
    ret,frame = video.read()
    if ret == True:
        cv2.imshow('frame',funcs.grabcut(frame))
        funcs.calc_hist(funcs.grabcut(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()