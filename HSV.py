# Code to show HSV and concepts of extracting 
# features of a frame by varying hsv

import os
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def convertToHSV():
    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\car2.jpg')

    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV) #convert from BGR to HSV

    
    # Create a mask. Filtering for red color
    #lowerBound = np.array([0, 100, 100])   
    #upperBound = np.array([10, 255, 255])

    lowerBound = np.array([40, 0, 0])   
    upperBound = np.array([200, 150, 250])

    mask1 = cv.inRange(imgHSV, lowerBound, upperBound)

    cv.imshow('Orig', img)
    cv.imshow('Luminance 180', mask1)
    cv.waitKey(0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':  
    convertToHSV()