import cv2
import numpy as np 
import os 

### Circle detection with Hough Circles
# for some reason this program doesn't work that well (only detects very few circles)

os.chdir("/Users/macintosh/Desktop")

# load the image
image = cv2.imread("soccer.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 7)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 0.2)

for i in circles[0, :]:
	# draw the outer circle
	cv2.circle(image, (i[0], i[1]), int(i[2]), (255, 0, 0), 2) # the int is necesary for some reason

	# draw the center of the circle
	cv2.circle(image, (i[0], i[1]), int(2), (0, 255, 0), 5) # the int is necessary for some reason

cv2.imshow("Detected Circles", image)
cv2.waitKey()
cv2.destroyAllWindows()