import cv2
import numpy as np
from datetime import datetime
vid = cv2.VideoCapture(0);#0 is the port no
while(True):
    ret , frame = vid.read()
    cv2.imshow('frame' ,frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        if ret:
            cv2.imshow("Capture", frame)
            now = datetime.now()
            current_time = now.strftime("%H-%M-%S")
            cv2.imwrite("\images"+current_time + "mypic.jpg", frame)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
        else:
            print("no img saved")
    elif cv2.waitKey(1) & 0xFF == ord('q'): # 0xFF represents keyboard input key
        break
    elif cv2.waitKey(1) & 0xFF == ord('i'):

        # Read the images
        img = cv2.imread("\images"+current_time + "mypic.jpg")

        # Resizing the image
        image = cv2.resize(img, (700, 600))

        # Convert Image to Image HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Defining lower and upper bound HSV values
        lower = np.array([0, 164, 0])
        upper = np.array([179, 255, 255])

        # Defining mask for detecting color
        mask = cv2.inRange(hsv, lower, upper)

        # Display Image and Mask
        cv2.imshow("Image", image)
        cv2.imshow("Mask", mask)

        # Make python sleep for unlimited time
        cv2.waitKey(0)
vid.release()
cv2.destroyAllWindows()
vid = cv2.VideoCapture(0)
result , image = vid.read()