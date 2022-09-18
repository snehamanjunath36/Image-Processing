# imports
import cv2
import numpy as np
from datetime import datetime

# capture facility
vid = cv2.VideoCapture(0);#0 is the port no of the webcam of laptop

while(True):
    ret , frame = vid.read() #to read the image
    cv2.imshow('frame' ,frame) #show the image with output frame name 'frame'

    if cv2.waitKey(1) & 0xFF == ord('c'): #Keyboard command initialised for user
        if ret:
            cv2.imshow("Capture", frame) #another frame 'capture' is created
            now = datetime.now() 
            current_time = now.strftime("%H-%M-%S")
            cv2.imwrite("\images"+current_time + "mypic.jpg", frame) #image being saved in the given path
            cv2.waitKey(1000) # waits for 1 sec after the user command
            cv2.destroyAllWindows() #then destroys the 2nd window so created
        else:
            print("no img saved")
    elif cv2.waitKey(1) & 0xFF == ord('q'): # 0xFF represents keyboard input key
        break
    elif cv2.waitKey(1) & 0xFF == ord('i'):
        # Read the images
        # img = cv2.imread("\images"+current_time + "mypic.jpg")
        grayscale = cv2.imread("\images"+current_time + "mypic.jpg", cv2.IMREAD_GRAYSCALE)
        cv2.imshow("grayscale",grayscale)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
vid.release()
cv2.destroyAllWindows()
vid = cv2.VideoCapture(0)
result , image = vid.read()