from cv2 import rotate
import numpy as np 
import cv2 as cv 

img = cv.imread('C:/Users/DELL/Pictures/Screenshots/CM.png')
def translation(im , x , y):
    translation_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (im.shape[1], im.shape[0])
    return cv.warpAffine(im, translation_matrix, dimensions)

#cv.imshow('Rotated Conor', translation(img, 100 , -50))
ro = rotate(img , -90)
flipped = cv.flip(img , 0)
cv.imshow('Flipper', flipped)
cv.waitKey(0)
