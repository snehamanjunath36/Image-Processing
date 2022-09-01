import cv2
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
vid.release()
cv2.destroyAllWindows()
vid = cv2.VideoCapture(0)
result , image = vid.read()
