# Example code to convert to grayscale

import os
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def convertToGrayscale():
    # 3 Methods of Grayscale here
    #    Option #1: what is supported automatically in cv.imread
    #    Option #2: Using average
    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\tesla_car.png')

    imgOrig = cv.imread(imgPath)
    imgGrayscale = cv.imread(imgPath, cv.IMREAD_GRAYSCALE) #read as GS
    
    #cv.imshow('GrayScale Read', imgGrayscale)
    imgGrayscaleRGB = cv.cvtColor(imgGrayscale, cv.COLOR_BGR2RGB)
    imgOrigRGB = cv.cvtColor(imgOrig, cv.COLOR_BGR2RGB)

    # Here convert to grayscale using formula
    b,g,r = cv.split(imgOrig)

    # Formula GrayValue = 0.299 * Red + 0.587 * Green + 0.114 * Blue
    b_Option2 = (b * 0.114).round().astype(np.uint8)
    g_Option2 = (g * 0.587).round().astype(np.uint8)
    r_Option2 = (r * 0.299).round().astype(np.uint8)

    # collapsing 3 channels into 1
    imgGrayScaleOption2 = b_Option2 + g_Option2 + r_Option2  #grayscale using option 2
    imgGrayScaleOption3 = ((b + g + r)/3).round().astype(np.uint8)

    #cv.imshow('GrayScale Formula', imgGrayScaleFormula)
    #cv.waitKey(0)
    imgGrayScaleOption2 = cv.cvtColor(imgGrayScaleOption2, cv.COLOR_BGR2RGB)
    imgGrayScaleOption3 = cv.cvtColor(imgGrayScaleOption3, cv.COLOR_BGR2RGB)

    # You dont need to convert any grayscale since only 1 channel.
    # it whill show correctly in matplotlib and cv.imshow
    
    plt.figure()
    plt.subplot(231)
    plt.imshow(imgOrigRGB)
    plt.title("Original Image")
    plt.subplot(232)
    plt.imshow(imgGrayscaleRGB)
    plt.title("GrayScale at imread()")
    plt.subplot(233)
    plt.imshow(imgGrayScaleOption2)
    plt.title("GrayScale formula")
    plt.subplot(234)
    plt.imshow(imgGrayScaleOption3)
    plt.title("Average formula")
    plt.show()

    debug = 1

def grayScaleVideo():
    
    feed = cv.VideoCapture(0)
    
    # check if video camera is busy
    if not feed.isOpened():
        exit()

    while True:
        ret, frame = feed.read()
        
        # if ret is succesful read
        if ret:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow("My GrayScale Feed", frame)

        if cv.waitKey(1) == ord('q'):
            break
    
    # Release the camera   
    feed.release()

    # clean up any remaining windows
    cv.destroyAllWindows
    
if __name__ == '__main__':
    convertToGrayscale()
    #grayScaleVideo()