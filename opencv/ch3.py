import cv2 as cv
import numpy as np

black = np.zeros((500, 500, 3) , dtype='uint8')
cv.rectangle(black ,(0,0) , (100,150) , (255, 0, 0) , thickness=5)
cv.circle(black , (black.shape[1]//2 ,black.shape[0]//2) , 20 , (255, 255, 255) , thickness=-1)
cv.putText(black , 'Arnav',(black.shape[1]//2 ,black.shape[0]//2) , cv.FONT_HERSHEY_PLAIN, 1.0 , (255, 0,0), thickness=2 )
cv.imshow('Black', black)


cv.waitKey(0)