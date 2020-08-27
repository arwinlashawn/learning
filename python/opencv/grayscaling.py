import os
import cv2
import numpy as np

# set cwd to Desktop
os.chdir("/Users/macintosh/Desktop")

# save an image to a variable
input = cv2.imread("cstudy.jpg")

# # let's use the image we previously loaded
# to do the grayscale conversion
gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

# show the converted image!
cv2.imshow('grayscale_cstudy.jpg', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

# easier way to convert color image to grayscale, use "0" argument for imread
gray_image2 = cv2.imread("cstudy.jpg", 0) # no need to type cv2.COLOR_BGR2GRAY
cv2.imshow('grayscale_cstudy2', gray_image2)
cv2.waitKey()
cv2.destroyAllWindows()

# grayscaling is done to speed up processing time! (less information)

