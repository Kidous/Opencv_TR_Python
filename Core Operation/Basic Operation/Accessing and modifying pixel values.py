# -*- coding: utf-8 -*- 
# @Time : 2019/2/28 13:05 
# @Author : Mengqi 
# @Function : 
# @File : Accessing and modifying pixel values.py 
# @Software: PyCharm
import  cv2
import numpy as np

img = cv2.imread('aurora.jpg')

cv2.namedWindow('Original')
cv2.imshow('Original', img)
cv2.waitKey()
cv2.destroyWindow('Original')

cv2.namedWindow('Changed')
px = img[100,100]
print(px)
print(img.dtype)
#accessing only blue pixel
blue = img[100,100,0]
print(blue)

img[100,100] = [255, 255, 255]
print (img[100,100])

# Accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2), 50)

# Shape of image
print(img.shape)

# total number of pixels
print(img.size)

# image datatype
print(img.dtype)

# Certain operation on region of image
# ROI = img[280:340, 330:390]
# # img[373:333, 100:160] = ROI
# #
# # cv2.imshow('Changed', img)
# # cv2.waitKey()
# # cv2.destroyAllWindows()

## Splitting and merging umage channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# b = img[:,:,0]
##

