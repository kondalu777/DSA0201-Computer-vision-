import cv2

import numpy as np

img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3, 3), 0)

sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)

sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

sobel = np.sqrt(sobelx**2 + sobely**2)

thresh = cv2.threshold(sobel, 50, 255, cv2.THRESH_BINARY)[1]

kernel = np.ones((3,3),np.uint8)

dilation = cv2.dilate(thresh, kernel, iterations=1)

erosion = cv2.erode(dilation, kernel, iterations=1)

boundary = cv2.absdiff(dilation, erosion)

cv2.imshow('Boundary', boundary)

cv2.waitKey(0)

cv2.destroyAllWindows()
