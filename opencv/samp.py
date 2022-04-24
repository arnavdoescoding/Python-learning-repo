from cv2 import imshow
import numpy as np
import cv2 as cv
import math as m

# Creating the shape to be analyzed

image = cv.imread('C:/Users/DELL/Desktop/Sample.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

image[thresh == 255] = 0

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
erosion = cv.erode(image, kernel, iterations = 1)

cv.imshow('E', erosion)
new_image = cv.cvtColor(erosion , cv.COLOR_BGR2HSV) #We convert our image to hsv because BGR images are influenced by light falling , hue , saturation
lower_red = np.array([0, 0 , 0])
high_red = np.array([0 , 138, 255])
mask = cv.inRange(erosion, lower_red, high_red)
masked_image = cv.bitwise_and(erosion,erosion, mask=mask)
cv.imshow('masked_data', masked_image)
counter = 0
total = 0
data_array = np.asarray(masked_image)
for x in data_array:
    for y in x:
        if y[0] != 0 or y[1] != 0 or y[2] != 0:
            counter = counter + 1
        else:
            total = total + 1



square_root = m.sqrt(counter)
print(square_root)
cv.waitKey(0)
cv.destroyAllWindows()