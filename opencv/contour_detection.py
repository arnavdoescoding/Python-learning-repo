import numpy as np
import cv2 as cv 

img = cv.imread('C:/Users/DELL/Pictures/Screenshots/CM.png')
greyed = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
edges = cv.Canny(greyed , 125 , 175)
cv.imshow('Edges', edges)
blank = np.zeros(img.shape,dtype='uint8')
contours , hierarchies = cv.findContours(edges , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank , contours , -1, (0 , 255, 0),thickness=1)
cv.imshow('Contoured', blank)
cv.waitKey(0)