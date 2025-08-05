import os
import matplotlib.pyplot as plt
import cv2 as cv



def resizeImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'picture\\download.jpg')

    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Select the headlight section
    headlightRegion = imgRGB[61:82, 190:230, :] #format [y1:y2, x1:x2]

    # Creating an array to show different scaling algo
    interpMethod = [
        cv.INTER_LINEAR,
        cv.INTER_CUBIC,
        cv.INTER_NEAREST,
        cv.INTER_AREA,
        cv.INTER_LANCZOS4
    ]
    interTitle = ['LINEAR', 'CUBIC', 'NEAREST', 'AREA', 'LANCZOS']

    plt.figure()
    plt.subplot(2,3,1)
    plt.title ('Original')
    plt.imshow(headlightRegion)
    
    height, width, channel = headlightRegion.shape

    scale = 4 # increase in size
    i = 1
    
    for index in range(len(interpMethod)):
        i = index + 2
        newHeight = int(height * scale)
        newWidth = int(width * scale)
        imgRGBResize = cv.resize(headlightRegion, (newWidth, newHeight), interpolation=interpMethod[index])
        
        plt.subplot(2,3,i)
        plt.title(interTitle[index])
        plt.imshow(imgRGBResize)
    
    plt.show()
    debug = 1




if __name__ == '__main__':
    resizeImage()
