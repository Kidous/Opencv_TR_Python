import cv2
import numpy as np

# cv2.namedWindow('image', cv2.WINDOW_)
cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
image = cv2.imread('blocks-col.png')
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()