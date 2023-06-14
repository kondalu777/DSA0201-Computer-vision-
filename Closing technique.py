import cv2

import numpy as np

img = cv2.imread("C:/Users/Dama Prasoona/Downloads/22.png", cv2.IMREAD_GRAYSCALE)

kernel_size = 3

kernel_shape = cv2.MORPH_RECT

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((kernel_size, kernel_size), np.uint8))

cv2.imshow('Closing', closing)

cv2.waitKey(0)

cv2.destroyAllWindows()
