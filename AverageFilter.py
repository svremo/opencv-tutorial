import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv
import numpy as np


def filterDemo():
    # Code to demonstrate average filter and its impact to image
    #   Load an image
    #   Setup a window with a slider to visually see the impact

    root = os.getcwd()
    imgPath = os.path.join(root, "picture\\tesla.png")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # Setup a display window with subplots
    # using matplotlib because they can display multiple images

    plt.figure()

    # [left, bottom, width, height]: Slider axis (left, bottom), slider dimension (width, height): 
    ax_slider = plt.axes([0.2, 0.02, 0.65, 0.05])

    # stepsize/valstep = 2 to return only odd numbers.  Some filters only work with odd kernel sizes
    slider = Slider(ax_slider, 'Kernel Size', 1, 11, valinit=1, valstep=2) 

    # Add the plots
    #   1. Original Image
    #   2. Average Filter
    #   3. Gaussian Filter
    #   4. Median Filter
    
    plt.subplot(221)
    plt.title('Original')
    plt.axis('off')
    plt.imshow(imgRGB)

    plt.subplot(222)
    imgFilterRGB = cv.blur(imgRGB, (1,1))
    plt.title('Average Filter')
    plt.axis('off')
    fig1 = plt.imshow(imgFilterRGB)

    plt.subplot(223)
    imgFilterRGBGaussian = cv.GaussianBlur(imgRGB, (1, 1), 0)
    plt.title('Gaussian Filter')
    plt.axis('off')
    fig2 = plt.imshow(imgFilterRGBGaussian)

    plt.subplot(224)
    imgFilterRGBMedian = cv.medianBlur(imgRGB, 1)
    plt.title('Median Filter')
    plt.axis('off')
    fig3 = plt.imshow(imgFilterRGBMedian)

    # Inner function to update the image based on slider value
    def update(val):
        print("Slider value:", val)
        imgFilterRGB = cv.blur(imgRGB, (int(val), int(val)))
        imgFilterRGBGaussian = cv.GaussianBlur(imgRGB, (11, 11), int(val))
        imgFilterRGBMedian = cv.medianBlur(imgRGB, int(val))

        fig1.set_data(imgFilterRGB)
        fig2.set_data(imgFilterRGBGaussian)
        fig3.set_data(imgFilterRGBMedian)

    # Callback for slider to update the images
    slider.on_changed(update)
    plt.show()
    

def gaussianKernel(kernelSize, sigma):
    kernel1d = cv.getGaussianKernel(kernelSize, sigma)  # Create a 1D Gaussian kernel
    kernel2d = np.outer(kernel1d, kernel1d)  # Create a 2D Gaussian kernel by outer product
    return kernel2d

def gaussianKernel3DPlot():
    # Code to demonstrate a 3D plot of a Gaussian kernel

    kernelSize = 51

    # How big the kernel is (matrix) and 8 = standard deviation/sigma
    kernel = gaussianKernel(kernelSize, 8)  # Bigger size will also show more detail when plotted
        
    x = np.arange(0,kernelSize,1)  # Create an array from 0 to kernelSize-1 step 1
    y = np.arange(0, kernelSize, 1)
    X, Y = np.meshgrid(x, y)  # Create a meshgrid for 3D plotting

    # Plot the images
    fig = plt.figure()
    plt.subplot(121)  # 1 row, 2 columns, first subplot
    plt.title('Gaussian Kernel 2D')
    plt.imshow(kernel)  # show the 2D Gaussian kernel

    ax = fig.add_subplot(122, projection='3d')  # projection=3d need to usd add_plot instead of subplot
    ax.plot_surface(X, Y, kernel, cmap='viridis')  # Plot the 3D surface
    ax.set_title('Gaussian Kernel 3D')

    plt.show()
    debug = 1


if __name__ == '__main__':
    #gaussianKernel3DPlot()
    filterDemo()