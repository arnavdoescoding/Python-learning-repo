import numpy as np
import cv2 as cv


img = cv.imread('C:/Users/DELL/Pictures/Screenshots/CM.png')
blank = np.zeros(img.shape[:2] , dtype='uint8')
b , g , r = cv.split(img)
blue = cv.merge([b , blank ,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red' , red)
cv.waitKey(0)    