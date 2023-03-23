import cv2
import numpy as np
def hacer_espejo(frame):
    return cv2.flip(frame,1)

def hacer_caricatura(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def ver_hulk(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    HULK_debil= np.array([40, 40, 40])
    HULK_fuerte = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, HULK_debil, HULK_fuerte)
    return cv2.bitwise_and(frame, frame, mask=mask)

def hacer_thresh(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold_value = 127
    max_value = 255
    ret, thresholded = cv2.threshold(gray, threshold_value, max_value, cv2.THRESH_BINARY)
    return thresholded

def aplicar_mascara(frame):
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.rectangle(mask, (100, 100), (300, 300), 255, -1)    
    return cv2.bitwise_and(frame, frame, mask=mask)

def pintar_red(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    return frame

def sepia(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    sepia = np.ones(frame.shape)
    sepia[:,:,0] *= 153
    sepia[:,:,1] *= 204
    sepia[:,:,2] *= 255
    sepia[:,:,0] *= normalized_gray
    sepia[:,:,1] *= normalized_gray
    sepia[:,:,2] *= normalized_gray
    return np.array(sepia, np.uint8)

def grabcut(frame):
    rect = (50, 50, 300, 400)
    mask = np.zeros(frame.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    new_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1, 0).astype('uint8')
    return frame * new_mask[:, :, np.newaxis]

def calc_hist(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)

    hist_img = np.zeros((256, 256, 3), dtype=np.uint8)

    for i in range(256):
        cv2.line(hist_img, (i, 256), (i, 256 - int(hist_norm[i][0])), (255, 255, 255), thickness=1)

    cv2.imshow('Histogram', hist_img)

    return hist_norm

def calc_hist_thresh(frame):
    hist = cv2.calcHist([frame], [0], None, [256], [0, 256])

    hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)

    hist_img = np.zeros((256, 256, 3), dtype=np.uint8)

    for i in range(256):
        cv2.line(hist_img, (i, 256), (i, 256 - int(hist_norm[i][0])), (255, 255, 255), thickness=1)

    cv2.imshow('Histogram', hist_img)

    return hist_norm