import cv2
def mwnd(name):
    cv2.moveWindow(name, 10,50)

img = cv2.imread('Imagen3.png', 1)
cv2.imshow('corazondemelon', img)
mwnd('corazondemelon')
cv2.waitKey(0)

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
cv2.imshow('escaladegrises', gris);
mwnd('escaladegrises')
cv2.waitKey(0)

HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
cv2.imshow('escaladegrises', HSV);
mwnd('escaladegrises')
cv2.waitKey(0)

YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV);
cv2.imshow('escaladegrises', YUV);
mwnd('escaladegrises')
cv2.waitKey(0)

YCRCB = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB);
cv2.imshow('escaladegrises', YCRCB);
mwnd('escaladegrises')
cv2.waitKey(0)


b, g, r = cv2.split(img);
cv2.imshow('escaladegrises', b);
cv2.waitKey(0)
cv2.imshow('escaladegrises', r);
cv2.waitKey(0)
cv2.imshow('escaladegrises', g);
cv2.waitKey(0)

src = cv2.merge([r,g,b]);
cv2.imshow('escaladegrises', src);
mwnd('escaladegrises')
cv2.waitKey(0);

cv2.destroyAllWindows(0);
