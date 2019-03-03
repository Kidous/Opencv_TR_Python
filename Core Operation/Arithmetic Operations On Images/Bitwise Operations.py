# -*- coding: utf-8 -*- 
# @Time : 2019/3/1 11:41 
# @Author : Mengqi 
# @Function : 
# @File : Bitwise Operations.py 
# @Software: PyCharm
import cv2
import numpy as np

img2 = cv2.imread('crop0.jpg')
img1 = cv2.imread('desk_bgimg.jpg')

if img1 is not None:
    print(1)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now Create a mask of logo and create its inverse mask also

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175,255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black- out the area of logo in ROI
# 取 roi 中与 mask 中不为傥的值对应的像素的值虽其他值为 0
# 注意䦈䭻必刪有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask = mask)
## 这里如果将img1 和img2 参数互相调换会报错，尺寸不匹配
# 取 roi 中与 mask_inv 中不为傥的值对应的像素的值虽其他值为 0。
# Take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


