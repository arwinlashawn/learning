import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")
cv2.imshow("Original", image) # for comparison

# create our sharpening kernel, we don't normalize since the 
# values in the matrix sum to 1
kernel_sharpening = np.array([[-1, -1, -1],
							 [-1, 9, -1],
							 [-1, -1, -1]])


#apply different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey()
cv2.destroyAllWindows()

