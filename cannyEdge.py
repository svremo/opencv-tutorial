import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv


def update_value(min, max, imgRGB, displayImg):
    # Redo the image with new min and max
    imgFiltered = cv.Canny(imgRGB, min, max)

    #Update the display image
    displayImg.set_data(imgFiltered)


def cannyEdge():

    # Demo the canny edge
    # Step 1: Read the image
    # Step 2: Setup the canny edge
    # Step 3: Setup a window w/ scroll bar

    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\face.png')
    
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Run the canny Edge.  Input: image, min threshold, max threshold
    imgCanny = cv.Canny(imgRGB, 0, 120)

    # Setup the Demo window
    plt.figure("Canny Edge Demo")
    plt.axis(False)
    
    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(imgRGB)

    plt.subplot(1,2,2)
    plt.title("Processed")
    displayImg = plt.imshow(imgCanny, cmap='gray')

    # Add a slider
    axisMin = plt.axes([0.2, 0.04, 0.65, 0.05])
    minSlider = Slider(axisMin, 'Min Threshold', 0, 255, valinit=0)

    axisMax = plt.axes([0.2, 0.00, 0.65, 0.05])
    maxSlider = Slider(axisMax, 'Max Threshold', 0, 255, valinit=120)

    # Set callback function. Use lambda to send more params
    minSlider.on_changed(lambda val: update_value(val, maxSlider.val, imgRGB, displayImg))
    maxSlider.on_changed(lambda val: update_value(minSlider.val, val, imgRGB, displayImg))

    # Show the canvas/plot
    plt.show()

if __name__ == "__main__":
    cannyEdge()