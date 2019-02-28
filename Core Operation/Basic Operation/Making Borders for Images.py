# -*- coding: utf-8 -*- 
# @Time : 2019/2/28 14:32 
# @Author : Mengqi 
# @Function : 
# @File : Making Borders for Images.py 
# @Software: PyCharm

import cv2
import  numpy as np
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]
img1 = cv2.imread('aurora.jpg')

replicate = cv2.copyMakeBorder(img1, 100, 100,100,100,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 100,100,100,100, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,100,100,100,100, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 100,100,100,100,cv2.BORDER_CONSTANT)

plt.subplot(231), plt.imshow(img1,'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate,'gray'), plt.title('Replicate')
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('Reflect')
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('Reflect101')
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('Wrap')
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('constant')
plt.show()