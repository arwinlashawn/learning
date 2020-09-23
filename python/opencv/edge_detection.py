import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg", 0) # remember, you wanna use grayscale images for things like this

### 3 edge detection methods ###
# sobel, laplacian, canny 
# best one is canny


### sobel
# extract sobel edges 
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5) # for x-axis
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5) # for y-axis

cv2.imshow("Original", image)
cv2.waitKey()
cv2.imshow("Sobel X", sobel_x)
cv2.waitKey()
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey()

# now we see how it looks like when we combine both vertical and horizontal edges
sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("sobel_OR", sobel_OR)
cv2.waitKey()

### laplacian
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)
cv2.waitKey()

### canny (notice that both laplacian and canny are pretty simple to implement)
# we need to provide two values: threshold1 and threshold2. Any gradient value larger
# than threshold2 is considered to be an EDGE. any value below threshold 1 is not 
# considered to be an edge
# values in between threshold 1 and threshold2 are either classified as edges or non-edges
# based on how their intensities are "connected". in this case, any gradient values below 
# 60 are considered non-edges whereas any values above 120 are considered edges

# note that canny uses GRADIENT VALUES AS THRESHOLDS
canny = cv2.Canny(image, 50, 120) # switch the thresholds up to see different results!
cv2.imshow("Canny", canny)
cv2.waitKey()

cv2.destroyAllWindows()

