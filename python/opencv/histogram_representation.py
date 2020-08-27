import cv2
import numpy as np 
import os
from matplotlib import pyplot as plt  

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")

cv2.imshow("cstudy", image)
cv2.waitKey()
cv2.destroyAllWindows()

# calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# plot a histogram, ravel() flattens our image array
# takes 2d array and converts it to 1d
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# viewing separate color channels
color = ('b', 'g', 'r')

# now separate the colors and plot each in the histogram
for i, col in enumerate(color):
	histogram2 = cv2.calcHist([image], [i], None, [256], [0,256])
	plt.plot(histogram2, color = col)
	plt.xlim([0,256])

plt.show() 

