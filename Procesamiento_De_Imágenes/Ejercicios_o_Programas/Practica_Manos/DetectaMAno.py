import cv2
import numpy as np

# Cargar el clasificador de la mano
hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml')

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Definir los colores a detectar (en formato HSV)
color_range = [
    ((0, 50, 50), (10, 255, 255)),     # Rojo
    ((20, 50, 50), (30, 255, 255)),    # Naranja
    ((45, 50, 50), (75, 255, 255)),    # Verde
    ((90, 50, 50), (130, 255, 255)),   # Azul
    ((140, 50, 50), (179, 255, 255))   # Morado
]

# Función para detectar el color más común en una imagen
def detect_color(img, ranges):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Inicializar el histograma de colores
    hist = np.zeros(len(ranges))
    # Calcular el histograma de colores para cada rango
    for i, (lower, upper) in enumerate(ranges):
        mask = cv2.inRange(hsv, lower, upper)
        hist[i] = cv2.countNonZero(mask)
    # Devolver el índice del color más común
    return np.argmax(hist)

# Ciclo principal
while True:
    # Capturar un cuadro de video
    ret, frame = cap.read()
    # Si no se pudo capturar un cuadro de video, salir del ciclo
    if not ret:
        break

    # Convertir el cuadro a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar la mano en el cuadro
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    # Si se detectó la mano, dibujar un rectángulo alrededor de ella y
    # detectar el color más común dentro del rectángulo
    if len(hands) > 0:
        for (x,y,w,h) in hands:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            hand_roi = frame[y:y+h, x:x+w]
            color_index = detect_color(hand_roi, color_range)
            color_name = ''
            if color_index == 0:
                color_name = 'Rojo'
            elif color_index == 1:
                color_name = 'Naranja'
            elif color_index == 2:
                color_name = 'Verde'
            elif color_index == 3:
                color_name = 'Azul'
            elif color_index == 4:
                color_name = 'Morado'
            cv2.putText(frame, color_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Mostrar el cuadro de video
    cv2.imshow('frame', frame)

    # Si se presiona la tecla 'q', salir del ciclo
    if cv2.waitKey(1) == ord('q'):
        break
# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
