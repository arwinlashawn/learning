import cv2   
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

# 2 ways to sort contours
# 1. by area
# 2. spatial

### sort contours by area ###

# load the image
image = cv2.imread("cstudy.jpg")
cv2.imshow('0 - Original Image', image)
cv2.waitKey()

# create a balck image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

# create a copy of our original image
original_image = image

# grayscale our image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find canny edges
edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey()

# find contours and print how many were found
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of contours found =" + str(len(contours)))   

# draw all contours
cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Coutours over blank image', blank_image)
cv2.waitKey()

# draw all contours over blank image
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', image)
cv2.waitKey()

cv2.destroyAllWindows()


# define function to display contour area
def get_contour_area(contours):
	# returns the areas of all contours as list
	all_areas = []
	for cnt in contours:
		area = cv2.contourArea(cnt)
		all_areas.append(area)
	return all_areas


# print the areas of the contours before sorting
print("Contour Areas before sorting")
print(get_contour_area(contours))
original_image = image

# sort contours large to small
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print("Contour Areas after sorting")
print(get_contour_area(sorted_contours))

# iterate over our contours and draw one at a time
for c in sorted_contours:
	cv2.drawContours(original_image, [c], -1, (255,0,0), 3)
	cv2.waitKey()
	cv2.imshow("Contours by Area", original_image)

cv2.waitKey()
cv2.destroyAllWindows()


### spatial sorting not included here