import cv2
import numpy as np 
import os

File_Name = ""  #name of the image file in string.
File_Path = r""  #path of the image file.
Angle = int("") #angle of rotation

exists = os.path.exists(File_Path)  #checks if path is valid.

if (exists == False):
    print("Path is invalid")
else:
    # Read image from the disk. 
    img = cv2.imread(File_Path) 

    # Shape of image in terms of pixels. 
    (rows, cols) = img.shape[:2] 

    # getRotationMatrix2D creates a matrix needed 
    # for transformation. We want matrix for rotation 
    # w.r.t center to 45 degree without scaling. 
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Angle, 1) 
    res = cv2.warpAffine(img, M, (cols, rows)) 

    cv2.imshow(File_Name, res)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
