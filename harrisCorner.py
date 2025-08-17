import os
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv
import numpy as np

def harrisCorner():
    root = os.getcwd()

    imgPath = os.path.join(root, "picture\\boxesPic.png")
    img = cv.imread(imgPath)

    # Corner Harris requires GrayScale (1-channel)
    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    
    # Convert to floating point because Corner Harris
    # results need and will lead to FP precision
    imgGray = np.float32(imgGray)

    # Run Harris Corner        
    harris = cv.cornerHarris(imgGray, blockSize=2, ksize=3, k=0.03)

    # Mark the Corners in red
    # Corners are defined as any point above .5% (0.005)
    # Use higher values for stronger detection, but some 
    # weak corners can get lost
    img[harris> 0.005 * harris.max()] = [0,0,255]  # [Blue, Green, Red]


    cv.imshow("Image", img)
    cv.imshow("Gray", np.uint8(imgGray)) # conversion will allow proper showing of image, else it will all be white
    cv.imshow("Harris Points", harris)
    cv.imshow("Overlay", img)

if __name__ == "__main__":
    harrisCorner()
