import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

# load the shape template or reference image
template = cv2.imread("triangle.jpg", 0)
cv2.imshow('Template', template)
cv2.waitKey()

# load the target image with the shapes we're trying to match
target = cv2.imread("shapes.png")
cv2.imshow('Target', target)
cv2.waitKey()
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

# threshold both images first before using cv2.findContours
ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

# find contours in template
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# we need to sort the contours by area so that we can remove the largest 
# contour which is the image outline
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# we extract the second largest contour which will be our template contour
template_contour = contours[1]

# extract contours from second target image
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
	# iterate through each contour in the target image and
	# use cv2.matchShapes to compare contour shapes
	match = cv2.matchShapes(template_contour, c, 1, 0.0)
	print(match)
	# if the match value is less than 0.15
	if match < 0.15:
		closest_contour = c
	else:
		closest_contour = []

# error here, not sure why
cv2.drawContours(target, [closest_contour], -1, (0, 255, 0), 3)
cv2.imshow("Output", target)
cv2.waitKey()
cv2.destroyAllWindows()