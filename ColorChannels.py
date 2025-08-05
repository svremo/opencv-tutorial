import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def colorChannels():
    # Show and Plot the different BGR channels independently

    # Create matrix 
    zeroes = np.zeros((100,100))
    ones = np.ones((100,100))

    blackImage = cv.merge((zeroes, zeroes, zeroes))
    whiteImage = cv.merge((255*ones, 255*ones, 255*ones))
    redImage = cv.merge((255*ones, zeroes, zeroes))
    greenImage = cv.merge((zeroes, 255*ones, zeroes))
    blueImage = cv.merge((zeroes, zeroes, 255*ones))

    plt.figure()
    plt.subplot(231)
    plt.imshow(blackImage)
    plt.title('black')

    plt.subplot(232)
    plt.imshow(whiteImage)
    plt.title('white')


    plt.subplot(233)
    plt.imshow(redImage)
    plt.title('red')


    plt.subplot(234)
    plt.imshow(greenImage)
    plt.title('green')


    plt.subplot(235)
    plt.imshow(blueImage)
    plt.title('blue')

    plt.show()

def bgrChannelGrayscale():

    

    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\example.png')

    img = cv.imread(imgPath)
    
    blue,green,red = cv.split(img)
    
    mask = blue & green & red
    blueOnly = mask ^ blue
    redOnly = mask ^ red
    greenOnly = mask ^ green

    #blueOnly = cv.bitwise_not(blueOnly)
    #greenOnly = cv.bitwise_not(greenOnly)
    #redOnly = cv.bitwise_not(redOnly)

    mergeImg = cv.merge((blueOnly, redOnly, greenOnly))

    zeros = np.zeros_like(blue)
    ones = np.ones_like(blue)

    blue_mask = cv.merge((zeros,255*ones,255*ones))

    cv.imshow('Orig',img)
    cv.imshow('Blue', blue)
    cv.imshow('Green', green)
    cv.imshow('Red', red)

    cv.imshow('BlueOnly', blueOnly)
    cv.imshow('greenOnly', greenOnly)
    cv.imshow('redOnly', redOnly)

    cv.imshow('Merged Image', mergeImg)

    
    blueRGB = cv.cvtColor(blue, cv.COLOR_BGR2RGB)
    redRGB = cv.cvtColor(red, cv.COLOR_BGR2RGB)
    greenRGB = cv.cvtColor(green, cv.COLOR_BGR2RGB)

    
    plt.figure()
    plt.subplot(231)
    plt.imshow(blueRGB)
    plt.title('blue component')

    plt.subplot(232)
    plt.imshow(greenRGB)
    plt.title('green component')


    plt.subplot(233)
    plt.imshow(redRGB)
    plt.title('red component')

    plt.show()
    debug = 1

def bgrChannelOnlyVisible():
    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\multiColor.jpg')

    img = cv.imread(imgPath)
    h, w, _ = img.shape

    # Split channels
    blue, green, red = cv.split(img)

    # Create a mask where the channel exists
    red_masked = np.where(red > 0, red, 255).astype(np.uint8)   # red areas show their intensity, background stays white
    green_masked = np.where(green > 0, green, 255).astype(np.uint8)
    blue_masked = np.where(blue > 0, blue, 255).astype(np.uint8)

    cv.imshow('Original', img)
    cv.imshow('Red Channel Visible', red_masked)
    cv.imshow('Green Channel Visible', green_masked)
    cv.imshow('Blue Channel Visible', blue_masked)

    cv.waitKey(0)
    cv.destroyAllWindows()

    """
    Explanation:
    - Pixels with red > 0 keep their grayscale intensity.
    - Pixels with no red remain white (255).
    - So only actual red parts appear, everything else stays white.
    """


if __name__ == '__main__':
    #colorChannels()
    bgrChannelGrayscale()
    #bgrChannelOnlyVisible()