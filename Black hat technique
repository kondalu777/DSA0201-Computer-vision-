import cv2

import numpy as np

img = cv2.imread("D:\computer vision\naruto.jpg", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Original Image', img)

cv2.imshow('Black-hat Transform', blackhat)

cv2.waitKey(0)

cv2.destroyAllWindows()
