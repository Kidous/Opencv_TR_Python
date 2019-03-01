# -*- coding: utf-8 -*- 
# @Time : 2019/3/1 11:25 
# @Author : Mengqi 
# @Function : 
# @File : Read or Write a figure inculding Chinese char.py 
# @Software: PyCharm

import cv2
import numpy as np
img_path = r"G:\Python_work\图片\vikings.jpg"
#img = cv2.imread(r"G:\Python_work\图片\vikings.jpg")
img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
#也可以写成cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)；
# cv2.IMREAD_UNCHANGED参数可以用-1代替
#cv2.IMREAD_GRAYSCALE:以灰度模式读入图像：其值为0
#cv2.IMREAD_COLOR:读入彩色图像：其值为1；
#np.fromfile()函数相对应的函数为np.tofile()
img_write = cv2.imencode(".jpg",img)[1].tofile(img_path)
#cv2.imencode()函数返回两个值;写入成功返回Ture，另一个值为数组.
#_,im_encode = cv2.imencode(".jpg",img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
