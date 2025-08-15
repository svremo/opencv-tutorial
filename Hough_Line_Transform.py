import os
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv
import numpy as np


def houghLine():
    # Read the image
    # Run Post processing
    # Run hough line to identify lines
    # Display results

    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\dash_view.png')

    # Read image as grayScale
    img = cv.imread(imgPath)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #convert from BGR --> RGB
    imgOrig = np.copy(img)

    # Apply some post processing
    # Not necessary to run Hough, but important
    # to remove details that can throw-off Hough
    imgBlur = cv.GaussianBlur(img,(3,3),2)
    imgCanny = cv.Canny(imgBlur, 203, 209) 

    # Run Hough Lines  
    r = 5  #distance in pixels from the origin of the line
    angle = np.pi/180 # how many degrees to sample. 1 degree
    threshold = 100 #Number of intersections 
    lines = cv.HoughLines(imgCanny,r,angle,250)

    # Iterate over each line from Houghs
    # Modify image with the line (overlayed)
    for line in lines:
        rho, theta  = line[0]
        print ("R: {}, Thetha: {}".format(rho, angle ))

        # Covert the polar coordinates to cartesian
        a = math.cos(theta)
        b = math.sin(theta)

        x0 = a * rho
        y0 = b * rho

        pt1 = (int (x0 + 1000 * (-b)), int(y0 + 1000*(a))) #tuple for x,y coordinate
        pt2 = (int (x0 - 1000 * (-b)), int(y0 - 1000*(a))) #tuple for x,y coordinate

        cv.line(img, pt1, pt2, (255, 0, 0)) # remember the image is in RGB


    # Display the results
    plt.figure()
    plt.subplot(221)
    plt.title("Original")
    plt.imshow(imgOrig)
    plt.subplot(222)
    plt.title("Gaussian Blur")
    plt.imshow(imgBlur)
    plt.subplot(223)
    plt.title("Canny Edge")
    plt.imshow(imgCanny)
    plt.subplot(224)
    plt.imshow(img)
    plt.title("Hough Line Overlay")

    plt.show()
    debug = 1 

# The additional functions below, I updated the above to have a Scrollbar
# To show the amount of effort to fine-tune the post-processing to have 
# allow Hough a decent line detection

def updateImages(t1val, t2val, kernel, sigma, img, imgBlurPlot, imgCannyPlot):
    kernelSize = (kernel, kernel)
    imgBlur = cv.GaussianBlur(img, kernelSize, sigma)
    imgCanny = cv.Canny(imgBlur, t1val,t2val)

    imgBlurPlot.set_data(imgBlur)
    imgCannyPlot.set_data(imgCanny)


def updateImagesHough(val, img, imgCanny, imgPlot):
    imgOrig = np.copy(img)
    r = 5  #distance in pixels from the origin of the line
    angle = np.pi/180 # how many degrees to sample. 1 degree
    threshold = val #Number of intersections 
    lines = cv.HoughLines(imgCanny,r,angle,threshold)


    for line in lines:
        rho, theta  = line[0]
        print ("R: {}, Thetha: {}".format(rho, angle ))

        # Covert the polar coordinates to cartesian
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a * rho
        y0 = b * rho

        pt1 = (int (x0 + 1000 * (-b)), int(y0 + 1000*(a))) #tuple for x,y coordinate
        pt2 = (int (x0 - 1000 * (-b)), int(y0 - 1000*(a))) #tuple for x,y coordinate

        cv.line(imgOrig, pt1, pt2, (0, 0, 255))
    
    imgPlot.set_data(imgOrig)

def houghLineWithScrollBar():
    # I'm adding this function to find a good kernel settings
    # before sending my image HougLines

    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\dash_view.png')

    # Read image as grayScale
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
 
    # Apply some post processing to
    imgOrig = np.copy(img)
    imgBlur = cv.GaussianBlur(img,(3,3),2)
    imgCanny = cv.Canny(imgBlur, 203, 209) 

    plt.figure()
    plt.subplot(2,4,1)
    plt.imshow(img)
    plt.subplot(2,4,2)
    imgBlurPlot = plt.imshow(imgBlur)
    plt.subplot(2,4,3)
    imgCannyPlot = plt.imshow(imgCanny, cmap='gray')

    r = 5  #distance in pixels from the origin of the line
    angle = np.pi/180 # how many degrees to sample. 1 degree
    threshold = 100 #Number of intersections 
    lines = cv.HoughLinesP(imgCanny,r,angle,100)

    for line in lines:
        rho, theta  = line[0]
        print ("R: {}, Thetha: {}".format(rho, angle ))

        # Covert the polar coordinates to cartesian
        a = np.sin(theta)
        b = np.cos(theta)

        x0 = a * rho
        y0 = b * rho

        pt1 = (int (x0 + 1000 * (-b)), int(y0 + 1000*(a))) #tuple for x,y coordinate
        pt2 = (int (x0 - 1000 * (-b)), int(y0 - 1000*(a))) #tuple for x,y coordinate

        cv.line(imgOrig, pt1, pt2, (0, 0, 255))


    plt.subplot(2,4,4)
    houghImagePlot= plt.imshow(imgOrig)
    
    # Add a slider
    kernelSize = plt.axes([0.2, 0.16, 0.65, 0.05])
    kernelSlider = Slider(kernelSize, 'Kernel Size', 1, 255, valinit=1, valstep=2)

    sigma = plt.axes([0.2, 0.12, 0.65, 0.05])
    sigmaSlider = Slider(sigma, 'Sigma', 0, 255, valinit=120, valstep=1)

    threshold1 = plt.axes([0.2, 0.08, 0.65, 0.05])
    t1Slider = Slider(threshold1, 'Threshold1', 1, 255, valinit=1, valstep=1)
    
    threshold2 = plt.axes([0.2, 0.04, 0.65, 0.05])
    t2Slider = Slider(threshold2, 'Threshold2', 1, 255, valinit=1, valstep=1)

    houghThreshold = plt.axes([0.2, 0.00, 0.65, 0.05])
    houghSlider = Slider(houghThreshold, 'Hough Threshold', 1, 255, valinit=150, valstep=1)

    # Assign Callback functions
    kernelSlider.on_changed(lambda val: updateImages (t1Slider.val, t2Slider.val, val, sigmaSlider.val, img, imgBlurPlot, imgCannyPlot))
    sigmaSlider.on_changed(lambda val: updateImages (t1Slider.val, t2Slider.val, kernelSlider.val, val, img, imgBlurPlot, imgCannyPlot))
    t1Slider.on_changed(lambda val: updateImages (val, t2Slider.val, kernelSlider.val, sigmaSlider.val, img, imgBlurPlot, imgCannyPlot))
    t2Slider.on_changed(lambda val: updateImages (t1Slider.val, val, kernelSlider.val, sigmaSlider.val, img, imgBlurPlot, imgCannyPlot))
    houghSlider.on_changed(lambda val: updateImagesHough (val, img, imgCanny, houghImagePlot))
    
    plt.show()


if __name__ == "__main__":
    houghLine()
    #houghLineWithScrollBar()