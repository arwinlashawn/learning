import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

# first, create a 3x3 kernel
kernel_3x3 = np.ones((3,3), np.float32) / 9

# we use the cv2.filter2D to convolve the kernel with a image
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey()

# secondly, create a 7x7 kernel
kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred2)
cv2.waitKey()

cv2.destroyAllWindows()

# other commonly used blurring methods in OpenCV (4 methods shown here)

# averaging done by convolvinf the image with a normalized box filter
# this takes the pixels under the box and replaces the central element
# box size needs to be odd and positive!
blur = cv2.blur(image, (3,3)) 
cv2.imshow("Averaging", blur)
cv2.waitKey()

# instead of box filer, gaussian kernel
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gaussian Blurring", Gaussian)
cv2.waitKey()

# takes median of all the pixels under kernel are and central
# element is replaced with this median value
# notice "paint" effect
median = cv2.medianBlur(image, 5)
cv2.imshow("Median Blurring", median)
cv2.waitKey()

# Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral Blurring", bilateral)
cv2.waitKey()

cv2.destroyAllWindows()

# Special section on image de-noising
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
cv2.imshow("Fast Means Denoising", dst)
cv2.waitKey()

cv2.destroyAllWindows()









