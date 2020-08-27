import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg", 0) # for best result use a black and white image with text
cv2.imshow("Original", image)
cv2.waitKey()

# first we need to define our kernel size
kernel = np.ones((2, 2), np.uint8)

# now we start erosion
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow("Erosion", erosion)
cv2.waitKey()

# this is for dilation
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow("Dilation", dilation)
cv2.waitKey()

# opening (good for removing noise)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey()

# closing (good for removing noise)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey()

cv2.destroyAllWindows()


