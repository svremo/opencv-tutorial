import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv


# Build another demo for thresholding
# Use the slider we just built from another demo to showcase
# the impact of different threshold values
# for the numerous thresholding methods

# Additional concepts shown:
#   sending parameters on callback function (update_threshold) using lambda
#   instead of nested function like in AverageFilter.py

def update_threshold(val, imGry, trshMthd, trshRst):
        for i in range(len(trshMthd)):
            ret, trsh = cv.threshold(imGry, int(val), 255, trshMthd[i])
            if ret:
                trshRst[i].set_data(trsh)

def thresholdDemo():
    root = os.getcwd()
    imgPath = os.path.join(root, "picture\\tesla_car.png")
    img = cv.imread(imgPath)
    
    # No need to convert current BGR encoding to RGB
    # since we are converting to grayscale
    # grayscale images are used most often in thresholding 

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    

    # Setup to arrays for the different methods
    threshMethods = [
        cv.THRESH_BINARY,             # pixel > threshold, max (white), else zero (black)
        cv.THRESH_BINARY_INV,         # pixel > threshold, zero (black), else max (white)
        cv.THRESH_TRUNC,              # pixel > threshold, threshold, else pixel
        cv.THRESH_TOZERO,             # pixel > threshold, zero (black), else pixel
        cv.THRESH_TOZERO_INV          # pixel > threshold, pixel, else zero (black)
    ]

    threshNames = ['BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    threshResult = [None] * len(threshMethods)    # Array to hold results

    
    plt.subplot(2,3,1)
    plt.title("Grayscale Image")
    plt.axis('off')  # do not show axis labels
    plt.imshow(imgGray,cmap='gray')  # Display grayscale image
    
    for i in range(len(threshMethods)):
        ret, thresh = cv.threshold(imgGray, 200, 255, threshMethods[i])

        if ret:
            plt.subplot(2, 3, i + 2)                           # 2 Rows, 3 columns
            threshResult[i] = plt.imshow(thresh, cmap='gray')  # Display thresholded image
            plt.title(threshNames[i])                          # title for each subplot
            plt.axis('off')                                    # do not show axis labels

    # Add a slider and a function to update the threshold value
    ax_slider = plt.axes([0.2, 0.02, 0.65, 0.05])
    slider = Slider(ax_slider, 'Threshold Value', 0, 255, valinit=200)

    slider.on_changed(lambda val: update_threshold(val, imgGray, threshMethods, threshResult))

    plt.show()

            
if __name__ == "__main__":
    thresholdDemo()