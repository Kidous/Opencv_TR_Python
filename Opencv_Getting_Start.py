# -*- coding: utf-8 -*- 
# @Time : 2019/2/24 19:06 
# @Author : Aries 
# @Site :  
# @File : Opencv_Getting_Start.py 
# @Software: PyCharm

import numpy as np
import cv2

img = cv2.imread('blocks-col.png', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('CopyOne.png', img)
    cv2.displayStatusBar()
