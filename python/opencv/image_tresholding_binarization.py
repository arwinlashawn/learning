import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image) # for comparison

# values  below 127 goes to 0 (black, everything above agoes to 255, white)
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)

# values below 127 go to 255 and values above 127 go to 0 (reverse of above)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse', thresh2)

# values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC', thresh3)

# values below 127 go to 0, above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO', thresh4)

# reverse of above, below 127 is unchanged, above 127 goes to 0
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV', thresh5)

cv2.waitKey()
cv2.destroyAllWindows()

### better alternative? ADAPTIVE THRESHOLDING ### 
# why? won't need to set the threshold manually

# for comparison
cv2.imshow("Original", image) # use an image with text for best result (picture of a page)

# good pratice to blur images as it removes noise
image = cv2.GaussianBlur(image, (3, 3), 0)

# time to apply adaptive threshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
								cv2.THRESH_BINARY, 3, 5)
cv2.imshow("Adaptive Mean Thresholding", thresh)
cv2.waitKey()

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", th2)
cv2.waitKey()

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(image, (5, 5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian Otsu's Thresholding", th3)
cv2.waitKey()

cv2.destroyAllWindows()








