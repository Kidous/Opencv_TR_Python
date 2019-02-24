# -*- coding: utf-8 -*- 
# @Time : 2019/2/24 19:28 
# @Author : Aries 
# @Site :  
# @File : Import Matplotlib.py 
# @Software: PyCharm

import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('blocks-col.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks(),plt.yticks()# to hide tick values on X and Y axis
plt.show()