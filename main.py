# import statement
import cv2
# capture facility
vid = cv2.VideoCapture(0);#0 is the port no
while(True):
    ret , frame = vid.read()
    cv2.imshow('frame' ,frame)
    if cv2.waitKey(1) & 0xFF == ord('i'): # 0xFF represents keyboard input key
        break
vid.release()
cv2.destroyAllWindows()