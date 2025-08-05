import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, r'picture\download.jpg')

    img = cv.imread(imgPath)    
    debug = 1
    cv.imshow('Image Show', img)
    cv.waitKey(0)


def writeImage():
    root = os.getcwd()
    imgPath = os.path.join(root, r'picture\download.jpg')

    img = cv.imread(imgPath)    
    debug = 1
    cv.imshow('Image Show', img)
    
    outPath = os.path.join(root, r'picture\output.jpg')
    cv.imwrite(outPath, img)



if __name__ == '__main__':
    #print (cv.__version__)
    #readImage()
    writeImage()