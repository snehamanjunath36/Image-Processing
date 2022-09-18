import tkinter
import cv2
from datetime import datetime
from tkinter import *
from tkinter.ttk import *



frame = Tk()
frame.title('fss')
frame.geometry("800x800")


def imgsave():
    vid = cv2.VideoCapture(0);
    ret, frame = vid.read()
    cv2.imshow("Capture", frame)
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    cv2.imwrite("\images" + current_time + "cap.jpg", frame)
    cv2.waitKey(3000)
    vid.release()


def imgquit():
    cv2.destroyAllWindows()

    # quit()

head = Label(frame, text="Hello User! Welcome")
head.pack()

btn1 = Button(frame,text = 'Click and Save',command = imgsave)
btn1.pack()

btn2 = Button(frame,text = 'Quit',command = imgquit)
btn2.pack()

btn3 = Button(frame,text = 'exit window',command = frame.quit)
btn3.pack()

mainloop()