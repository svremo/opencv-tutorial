# This is my first attemp on creating a video processing using openCV

import cv2 as cv
from cv2_enumerate_cameras import enumerate_cameras
import os 

def enumCameras():

    # This is code I got of gemini to enumerate and find the
    # camera index number 

    try:
        # CAP_DSHOW was the one that was able to show the right index for use in openCV
        cameraList = enumerate_cameras(cv.CAP_DSHOW)

        if cameraList:
            # print the info
            for camera in cameraList:
                print(f"  Index: {camera.index}")
                print(f"  Name: {camera.name}")
                print(f"  Path: {camera.path}")
                print(f"  Vendor ID: {hex(camera.vid) if camera.vid else 'N/A'}")
                print(f"  Product ID: {hex(camera.pid) if camera.pid else 'N/A'}")
                print(f"  Backend: {cv.videoio_registry.getBackendName(camera.backend)}")
                print("-" * 20)

    except Exception as e:
        print(f"Error enumerating cameras: {e}")
        print("This might happen if the backend is not supported or if there's a permission issue.")
        return []


def viewWebcam():
    # The index 0 here can be programatically determined (see enumCameras)
    # using 0 here based on trial and error

    feed = cv.VideoCapture(0)
    
    # check if video camera is busy
    if not feed.isOpened():
        exit()

    while True:
        ret, frame = feed.read()
        
        # if ret is succesful read
        if ret:
            cv.imshow("My Feed", frame)

        if cv.waitKey(1) == ord('q'):
            break
    
    # Release the camera   
    feed.release()

    # clean up any remaining windows
    cv.destroyAllWindows


def recordFromWebcam():
    # The index 0 here can be programatically determined (see enumCameras)
    # using 0 here based on trial and error
    feed = cv.VideoCapture(0)
    root = os.getcwd()
    vidOutPath = os.path.join(root, 'video\\sample.avi')
    encoding = cv.VideoWriter_fourcc(*'XVID')

    # 
    recording = cv.VideoWriter(vidOutPath, encoding, 30, (640,480))
    
    # check if video camera is busy
    if not feed.isOpened():
        exit()

    if not recording.isOpened():
        exit()

    while True:
        ret, frame = feed.read()
        
        # if ret is succesful read
        if ret:
            cv.imshow("My Feed", frame)
            recording.write(frame)
            

        if cv.waitKey(1) == ord('q'):
            break

    # Release the camera and recording   
    feed.release()
    recording.release()

    # clean up any remaining windows
    cv.destroyAllWindows


def readVideoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'video\\simple.avi')

    # Open the video
    feed = cv.VideoCapture(vidPath)

    while feed.isOpened():
        ret, frame = feed.read()
        if ret:  
            cv.imshow ('Video from file', frame)
        
        
        if cv.waitKey(10) == ord('q'):
            break
    
    


if __name__ == '__main__':
    viewWebcam()
    #recordFromWebcam()
    #enumCameras()
    #qreadVideoFromFile()