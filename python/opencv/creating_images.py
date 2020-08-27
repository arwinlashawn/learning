import cv2
import numpy as np 
import os
from matplotlib import pyplot as plt  

os.chdir("/Users/macintosh/Desktop")

# to draw a black square
image = np.zeros((512,512,3), np.uint8)

# to draw a black and white image (without 3d to create grayscale image
# output still black
image_bw = np.zeros((512,512), np.uint8) 

cv2.imshow("Black", image)
cv2.imshow("White", image_bw)

cv2.waitKey()
cv2.destroyAllWindows()

# first, draw a line over black square
image = np.zeros((512, 512, 3), np.uint8) # draws a black square
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
cv2.imshow("Blue Line", image)

cv2.waitKey()
cv2.destroyAllWindows() 

# now draw a rectangle
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 5) # -1 will fill the rectangle with the color
cv2.imshow("Rectangle", image)
cv2.waitKey()
cv2.destroyAllWindows()

# what about circle?
cv2.circle(image, (350,350), 100, (15,75,50), -1)
cv2.imshow("Circle", image)
cv2.waitKey()
cv2.destroyAllWindows()

# polygons?
# need to create an array of points
pts = np.array([[10,50], [400,50], [90,200], [50,500]], np.int32)

# let's now reshape our points in form required by polylines
pts = pts.reshape((-1,1,2)) # how polylines require the points to be stored

cv2.polylines(image, [pts], True, (0,0,255), 3)
cv2.imshow("Polygon", image)
cv2.waitKey()
cv2.destroyAllWindows()

# we can add text too!
cv2.putText(image, "Hello World!", (75,290), cv2.FONT_HERSHEY_PLAIN, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey()
cv2.destroyAllWindows()









