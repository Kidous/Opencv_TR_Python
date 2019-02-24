import cv2
import numpy as np

image = cv2.imread('blocks-col.png')

cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()