import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

# make our image 3/4th of its original size
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75) # linear interpolation by default
cv2.imshow('Scaling - Linear Interpolation', image_scaled)
cv2.waitKey()

# now double the image size
image_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', image_scaled)
cv2.waitKey()

# now skew the re-sizing by setting exact dimensions
image_scaled = cv2.resize(image, (900,100), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()