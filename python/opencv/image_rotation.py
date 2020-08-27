import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")
height, width = image.shape[:2]

# now divide by two to rotate the image around its center
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# will notice that image dimensions exceed frame after rotation
# can change 1 to .5 (scaling factor) so whole image can fit into frame
# alternative is to use fully transpose the image, NO BLACK SPACE!

rotated_image = cv2.transpose(image)
cv2.imshow("Rotated Image 2", rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
# NO BLACK SPACE IS SEEN!