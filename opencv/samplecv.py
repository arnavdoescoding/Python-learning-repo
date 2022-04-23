import cv2 as cv
from cv2 import threshold 
import numpy as np 
img = cv.imread('C:/Users/DELL/Desktop/Sample.png')
img_g = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
black = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Static Scan Greyscale", img_g)
threshold, thresh = cv.threshold(img_g, 150 , 255 , cv.THRESH_BINARY)
cv.imshow("Static Scan Greyscale", thresh)

cv.waitKey(0)