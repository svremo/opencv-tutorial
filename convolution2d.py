import os
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def convolution2D():

    # Run through 3 examples of using filter2D / 2D convolution
    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\car2.jpg')

    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Blur Example
    n = 3
    kernel = np.ones((n,n), np.float32)/(n*n)
    blurImage = cv.filter2D(imgRGB, -1, kernel)

    # Sharpen Image
    kernel = np.array([[0, -1,  0],
                      [-1,  5, -1],
                      [0,  -1,  0]])
    
    sharpenImage = cv.filter2D(imgRGB, -1, kernel)
    
    # Edge Detection
    # this is one possible mask
    #kernel = np.array([[-1, 0,  1],
    #                   [-2, 0, 2],
    #                   [-1, 0, 1]])
    #

    # for my example, this mask was better
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

    edgeImage = cv.filter2D(imgRGB, -1, kernel)

    # Plot each images for comparison
    plt.figure()
    plt.subplot(2,2,1)
    plt.title ('Orig')
    plt.imshow(imgRGB)

    plt.subplot(2,2,2)
    plt.title('Blurred Image')
    plt.imshow(blurImage)

    plt.subplot(2,2,3)
    plt.title('Sharpened Image')
    plt.imshow(sharpenImage)

    plt.subplot(2,2,4)
    plt.title('Edge Detection')
    plt.imshow(edgeImage)

    plt.show()

if __name__ == '__main__':
    convolution2D()
    