import cv2
from datetime import datetime
vid = cv2.VideoCapture(0)
result , image = vid.read()
if result:
    cv2.imshow("Capture",image)
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    cv2.imwrite(current_time+"mypic.jpg", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
else:
    print("no img saved")