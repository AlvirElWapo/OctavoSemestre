import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('Imagen3.png')

# Convert the image to 5 different colorspaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

# Show each image and its histogram
for i, (name, colorspace) in enumerate([('gray', gray), ('hsv', hsv), ('lab', lab), ('yuv', yuv), ('xyz', xyz)]):
    plt.subplot(2, 5, i+1)
    plt.imshow(colorspace)
    plt.title(name)
    plt.axis('off')
    plt.subplot(2, 5, i+6)
    plt.hist(colorspace.ravel(), bins=256, range=(0, 255))
    plt.title('Histogram')
    plt.xlim([0, 255])

# Show the plots
plt.show()

