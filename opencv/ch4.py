import cv2 as cv 
import numpy as np 

img = cv.imread('C:/Users/DELL/Pictures/Screenshots/CM.png')
#cv.imshow('Conor' , img )

grey_image = cv.cvtColor(img , cv.COLOR_BGR2GRAY) #Greying an image
#cv.imshow('Grey Conor', grey_image)
blurred_img = cv.GaussianBlur(img , (3,3), cv.BORDER_DEFAULT)  #Blurring an image
cv.imshow('Blurred Conor', blurred_img)
edges = cv.Canny(blurred_img , 125 , 175)
cv.imshow('Canny Edges' , edges)
cv.waitKey(0)