from cv2 import imshow
import numpy as np
import cv2 as cv

image = cv.imread('C:/Users/DELL/Desktop/Sample.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

image[thresh == 255] = 0

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
erosion = cv.erode(image, kernel, iterations = 1)

cv.imshow('E', erosion)
new_image = cv.cvtColor(erosion , cv.COLOR_BGR2HSV) #We convert our image to hsv because BGR images are influenced by light falling , hue , saturation
lower_red = np.array([0, 138 , 252])
high_red = np.array([0 , 138, 255])
mask = cv.inRange(erosion, lower_red, high_red)
cv.imshow('Mask', mask)


cv.waitKey(0)
cv.destroyAllWindows()