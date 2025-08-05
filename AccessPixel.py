import cv2 as cv
import matplotlib.pyplot as plt
import os


def plotImage():
    root = os.getcwd()
    imgPath = os.path.join(root, "picture\\download.jpg")
    img = cv.imread(imgPath)

    cv.imshow("Picture", img)

    # Do the BGR to RGB conversion
    # openCV uses BGR while matplot uses RGB
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Plot the image
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    headlightPixel = imgRGB[71,210]
    imgRGB[71,210] = [255,0,0]
    
    # Access, copy and paste a region
    headlightRegion = imgRGB[61:79, 192:229] #format [y1:y2, x1:x2]

    # compute the size of the space
    dy = 79-61
    dx = 229-192

    startx = 230
    starty = 62

    # Paste the copied region
    imgRGB[starty:starty+dy, startx:startx+dx] = headlightRegion





    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    plotImage()
    pass