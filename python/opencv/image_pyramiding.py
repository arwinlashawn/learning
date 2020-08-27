import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('Original', image)
cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger) # quality lost! 
cv2.waitKey()
cv2.destroyAllWindows()

# shows that re-sizing images can cause loss of quality

