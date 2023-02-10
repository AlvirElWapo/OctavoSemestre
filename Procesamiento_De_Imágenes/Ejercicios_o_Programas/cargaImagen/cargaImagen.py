import cv2

img = cv2.imread('/home/alvirelwapo/Pictures/wallpapers/wallpaper_3.jpg', 1)
cv2.imshow('corazondemelon', img)
cv2.waitKey(0)

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
cv2.imshow('escaladegrises', gris);
cv2.waitKey(0)

HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
cv2.imshow('escaladegrises', HSV);
cv2.waitKey(0)

YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV);
cv2.imshow('escaladegrises', YUV);
cv2.waitKey(0)

YCRCB = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB);
cv2.imshow('escaladegrises', YCRCB);
cv2.waitKey(0)


b, g, r = cv2.split(img);
cv2.imshow('blue', b);
cv2.waitKey(0)
cv2.imshow('red', r);
cv2.waitKey(0)
cv2.imshow('green', g);
cv2.waitKey(0)

src = cv2.merge([r,g,b]);
cv2.imshow('ImagenMerge', src);
cv2.waitKey(0);

cv2.destroyAllWindows(0);
