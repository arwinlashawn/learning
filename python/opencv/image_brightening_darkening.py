import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

# arithmetic operations

# create a matrix of ones, then multiply it by a scaler of 100
# this gives a matrix with the same dimensions of our image with all values being 100
M = np.ones(image.shape, dtype = "uint8") * 75

# to add matrix M to image
# notice the increase in brightness
added = cv2.add(image, M)
cv2.imshow("Added", added)

# likewise we can also subtract
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey()
cv2.destroyAllWindows()












