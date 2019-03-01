# -*- coding: utf-8 -*- 
# @Time : 2019/3/1 10:43 
# @Author : Mengqi 
# @Function : Image Blending
# @File : Arithmetic Operation on Images.py 
# @Software: PyCharm
import cv2
import numpy as np

img = cv2.imread('boy.jpg')
img1 = cv2.imread('girl.jpg')
h,w,_ = img1.shape

# cv2.imshow('Original', img1)
# cv2.waitKey()
# cv2.destroyWindow()

# print(img1.size)
# print(img2.size)

# Resize img based on img1
img2 = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
dst = cv2.addWeighted(img2,0.65,img1,0.55,0)
cv2.imshow('dst',dst)
cv2.imwrite('CopyOne.png',dst)
cv2.waitKey()
cv2.destroyAllWindows()