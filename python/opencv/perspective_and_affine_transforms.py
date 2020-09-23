import cv2
import numpy as np 
import os 
import matplotlib.pyplot as plt

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg", 0) # example image would be a piece of paper captured in the direction of one of its corners

cv2.imshow("Original", image)
cv2.waitKey()

### starting with perspective/non-affine transform
# assuming we have the coordinates of the four corners of the paper
points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

# coordinates of the 4 corners of the desired output
# we use a ratio of an A4 paper 1:41
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

# use the two sets of four points to compute 
# the perspective transformation matrix M
M = cv2.getPerspectiveTransform(points_A, points_B) # generates a matrix for transformation from A to B

warped = cv2.warpPerspective(image, M, (420, 594)) # to use the matrix to generate the output image
# (420, 594) is the final size of the image we wanna see

cv2.imshow("warpPerspective", warped)
cv2.waitKey()
cv2.destroyAllWindows()

# improvement: can write an algo that gets the contour of the image and automatically
# gets the coordinates of the corner points! (for points_A)

### now for affine transform
# you only need 3 coordinates instead of 4! (makes sense right?)

rows, cols = image.shape

cv2.imshow("Original", image)
cv2.waitKey()

# coordinates of 3 of the 4 corners of the original image
points_A = np.float32([[320, 15], [700, 215], [85, 610]])

# coordinates of 3 of the 4 corners of the desired output
# we use a ratio of an A4 paper 1:1.41
points_B = np.float32([[0, 0], [420, 0], [0, 594]])


# use the two sets of 3 points to compute the 
# Perspective Transformation Matrix, M
M = cv2.getAffineTransform(points_A, points_B)

warped = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow("warpAffine", warped)
cv2.waitKey()
cv2.destroyAllWindows()














