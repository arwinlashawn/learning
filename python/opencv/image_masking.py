import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

# bitwise operations (for image masking)
# handy when you need to mask images

# to demonstrate bitwise operations

# first make a grayscale square
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey()

# to draw an ellipse (but half)
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey()

cv2.destroyAllWindows()

# time to mess around with some bitwise operations

# shows only where the two shapes intersect
And = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", And)
cv2.waitKey()

# shows where either square or ellipse is
bitwiseOr = cv2.bitwise_or(square, ellipse)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey()

# shows where either exists by itself
bitwiseXor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey()

# shows everything that isn't part of one shape (in this case, square)
bitwiseNot_sq = cv2.bitwise_not(square)
cv2.imshow("NOT (square)", bitwiseNot_sq)
cv2.waitKey()

cv2.destroyAllWindows()








