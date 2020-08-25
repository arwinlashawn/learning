import os
import cv2
import numpy as np

# set cwd to Desktop
os.chdir("/Users/macintosh/Desktop")

# save an image to a variable
input = cv2.imread("cstudy.jpg")

# let's have a look at the invdividual color levels for the first pixel (0,0)

# BGR values for the first 0,0 pixel
B, G, R = input[0, 0]
print(B, G, R)

# to see dimenstions and color values
print(input.shape)

# what if we convert the image to grayscale?
gray_img = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
print(gray_img.shape) # output shows it is 2d array: (366, 489)
print(gray_img[10,50]) # outputs only one value: 239

# let's mess around with HSV color space
hsv_img = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_img)
cv2.imshow('Hue channel', hsv_img[:, :, 0]) # 0 specifies hue channel and so on
cv2.imshow('Saturation channel', hsv_img[:, :, 1])
cv2.imshow('Value channel', hsv_img[:, :, 2]) # shows GRAYSCALE version of the image
### Output ###
# hue channel is quite dark because only goes from 0-180
# note that anytime you use the imshow function, it tries to show the image
# as a BGR image. so it doesn't display HSV image properly

cv2.waitKey()
cv2.destroyAllWindows()

# now let's look at individual channels in an RGB channel (also possible)
B, G, R = cv2.split(input) # split image into individual channels

# let's see how they look like (spoiler, will show grayscale because they will be 1-D)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey()
cv2.destroyAllWindows()

# let's get the original image back by merging
merged_img = cv2.merge([B, G, R])
cv2.imshow("Merged Image", merged_img)

# an example of how filtering works, add 100 to blue
merged_img = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged_img)

cv2.waitKey()
cv2.destroyAllWindows()

# so how do we see individual channels as colors, not grayscale?
B, G, R = cv2.split(input)

# now let's create an array of zeros that are the same shape as the original image
# with dimensions of the image height x width
zeros = np.zeros(input.shape[:2], dtype = "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
# output images are now in blue, green and red respectively!

cv2.waitKey()
cv2.destroyAllWindows()












