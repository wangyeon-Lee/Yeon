# 수정

import cv2
import numpy as np

# image = np.full(480, 640, 3),255, np.uint8)
# cv2.imshow('white', image)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
# image = np.full(480, 640, 3),(0,0,255), np.uint8)
# cv2.imshow('white', image)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
image[240, 160] = image[240, 320] = image[240, 480] = (255, 255, 255)
cv2.imshow('black with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()

# # #2 imapge
# # image = cv2.imread('../Crawling/img/lena.png')
# image = cv2.imread('../Crawling/img/lena.png', 0)
# image = image.astype(np.float32) / 255
#
# gamma = 0.3
# corrected_image = np.power(image, gamma)
#
# cv2.imshow('image', image)
#
# print('Shape: ', image.shape)
# print('Data type: ', image.dtype)
#
# # image[:,:, [0, 2]] = image[:,:, [2, 0]]
# # cv2.imshow('blue_and_red_swapped', image)   # blue
#
# # cv2.imshow('image', np.clip(image*2,0,1))
#
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# # cv2.imshow('image', gray)
#
# cv2.imshow('image', image)
# cv2.waitKey()
# cv2.destroyAllWindows()
