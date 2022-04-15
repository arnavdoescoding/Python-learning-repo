from configparser import Interpolation
import numpy as np 
import pandas as pd
import cv2 as cv 

img = cv.imread('C:/Users/DELL/Pictures/Screenshots/CM.png')

def resizedImg(frame , scale=0.8):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)
    resized = cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)
    return resized

reimg = resizedImg(img)
cv.imshow('SMOL' , reimg)




cv.waitKey(0)

