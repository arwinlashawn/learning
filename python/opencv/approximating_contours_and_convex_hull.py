import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

# load image and keep a copy
image = cv2.imread("cstudy.jpg")
orig_image = image.copy()
cv2.imshow("Original image", orig_image)
cv2.waitKey()

# to binarize the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# iterate through each contour and compute the bounding rectangle
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	cv2.rectangle(orig_image, (x,y), (x+w, y+h), (0,0,255), 2)
	cv2.imshow("Bounding Rectangle", orig_image)

cv2.waitKey()

# iterate through each contour and compute the approx color
for c in contours:
	# calculate the accuracy as a percentage of the contour perimeter
	accuracy = 0.001 * cv2.arcLength(c, True) # the lower the value, the more precise the approximation
	approx = cv2.approxPolyDP(c, accuracy, True)
	cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
	cv2.imshow("Approx Poly DP", image)

cv2.waitKey()
cv2.destroyAllWindows()


### convex hull

# show original image
image = cv2.imread("cstudy.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)
cv2.waitKey()

# threshold the image
ret, thresh = cv2.threshold(gray, 176, 255, 0)

# find contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# sort contours by area and then remove the largest frame contour
n = len(contours) - 1
contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

# iterate through contours and draw the convex hull
for c in contours:
	hull = cv2.convexHull(c)
	cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
	cv2.imshow("Convex Hull", image)

cv2.waitKey()
cv2.destroyAllWindows()









