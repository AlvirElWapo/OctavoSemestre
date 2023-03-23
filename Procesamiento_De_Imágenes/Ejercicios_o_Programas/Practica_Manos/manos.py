import cv2
import numpy as np

cap = cv2.VideoCapture(-1)

while(True):
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Find contours of hand
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=cv2.contourArea)

    # Draw contour on frame
    cv2.drawContours(frame, [contours], -1, (0, 255, 0), 2)

    # Define color ranges to detect
    lower_blue = np.array([100, 0, 0])
    upper_blue = np.array([255, 50, 50])
    lower_green = np.array([0, 100, 0])
    upper_green = np.array([50, 255, 50])
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([50, 50, 255])

    # Create mask for each color and apply to frame
    mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
    mask_green = cv2.inRange(frame, lower_green, upper_green)
    mask_red = cv2.inRange(frame, lower_red, upper_red)
    frame_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    frame_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    frame_red = cv2.bitwise_and(frame, frame, mask=mask_red)

    # Display frames and histograms
    cv2.imshow('Original', frame)
    cv2.imshow('Blue', frame_blue)
    cv2.imshow('Green', frame_green)
    cv2.imshow('Red', frame_red)
    cv2.imshow('Edges', edges)
    hist_blue = cv2.calcHist([frame_blue], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([frame_green], [0], None, [256], [0, 256])
    hist_red = cv2.calcHist([frame_red], [0], None, [256], [0, 256])
    cv2.imshow('Blue Histogram', hist_blue)
    cv2.imshow('Green Histogram', hist_green)
    cv2.imshow('Red Histogram', hist_red)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
