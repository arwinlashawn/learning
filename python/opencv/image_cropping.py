import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

image = cv2.imread("cstudy.jpg")
height, width = image.shape[:2]

# set starting pixel coordinates for cropping (top left)
start_row, start_col = int(height * 0.15), int(width * 0.25)
print(start_row, start_col)

# set ending pixel coordinates for cropping (bottom right)
end_row, end_col = int(height * 0.65), int(width * 0.65)

# now simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow("Original", image)
cv2.waitKey()
cv2.imshow("Cropped", cropped) # output shows the face
cv2.waitKey()
cv2.destroyAllWindows()

