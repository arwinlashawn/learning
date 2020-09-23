import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg", 0) # good example would be to load a simple image with 3 black squares
cv2.imshow("Input image", image)
cv2.waitKey()

# find Canny edges
edged = cv2.Canny(image, 30, 200)
cv2.imshow("Canny edges", edged)
cv2.waitKey()

# find contours
# use a copy of the image e.g. edged.copy(), since findContours alters the image!
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny Edges After Contouring", edged)
cv2.waitKey()
print(contours)
print("Number of Contours found = " + str(len(contours)))

# time to draw all contours
# use -1 as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow("Contours", image)
cv2.waitKey()
cv2.destroyAllWindows()



