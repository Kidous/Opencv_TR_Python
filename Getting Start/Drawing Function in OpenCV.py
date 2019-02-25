# -*- coding: utf-8 -*- 
# @Time : 2019/2/25 11:00 
# @Author : Mengqi 
# @Function : 
# @File : Drawing Function in OpenCV.py 
# @Software: PyCharm
import cv2
import numpy as  np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511,511),(255,0,0),5)

# Draw a rectangle
img = cv2.rectangle(img, (384,0), (510, 128),(0,255,0), 3)

# Draw a circle
img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

# Draw an ellipse
img = cv2.ellipse(img, (256, 256), (100,50), 0,0,180,255,-1)

# Draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20],[50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))
## cv2.polylines() can be used to draw multiple lines.
# Just create a list of all the lines you want to draw and pass it to the function.
# All lines will be drawn individually.
# It is more better and faster way to draw a group of lines than calling cv2.line() for each line.


# Add text to images
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV',(10, 500),font,4, (255, 255,255),2, cv2.LINE_AA)

cv2.imshow('line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()