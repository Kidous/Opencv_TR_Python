# -*- coding: utf-8 -*- 
# @Time : 2019/2/24 19:39 
# @Author : Mengqi
# @Site :  
# @File : Getting Start with Video.py 
# @Software: PyCharm
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc()


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(".\capture.jpg", frame)
        print("Capture is successful\n")
        break
    elif cv2.waitKey(1) & 0xFF == ord('b'):
        cv2.imwrite(".\capture.jpg", frame)
        print("Capture is successful\n")
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()