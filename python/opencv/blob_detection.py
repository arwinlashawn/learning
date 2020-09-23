import cv2
import numpy as np 
import os

### Don't know why OUTPUT image isn't showing?

os.chdir("/Users/macintosh/Desktop")

# load the image
image = cv2.imread("sunflower.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)
cv2.waitKey()

# set up the detector with default parameters
detector = cv2.SimpleBlobDetector()

# detect blobs
keypoints = detector.detect(image)

# draw detected blobs as red circles
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle 
# corresponds to the size of blob
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# show keypoints!
cv2.imshow("Blobs", blobs)
cv2.waitKey()
cv2.destroyAllWindows()