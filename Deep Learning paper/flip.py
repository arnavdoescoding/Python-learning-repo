from typing import final
from scipy import ndimage
import cv2 
import os
import numpy as np 


from pathlib import Path
path_of_the_directory = 'C:/Users/DELL/Desktop/Stage4'
print("Files and directories in a specified path:")
file = Path(path_of_the_directory ).glob('*')
def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result




for i in file: 
    x = 5
    while x <= 350:

        img = cv2.imread(str(i))
        fin = str(i)[:-5] + str(x)+ '.jpeg'
        image_center = tuple(np.array(img.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, x, 1.0)
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
        x = x + 5
        cv2.imwrite(fin , result)


