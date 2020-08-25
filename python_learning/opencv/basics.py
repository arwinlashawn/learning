import os
import cv2
import numpy as np

# set cwd to Desktop
os.chdir("/Users/macintosh/Desktop")

# save an image to a variable
input = cv2.imread("cstudy.jpg")

# to display the image, use imshow
# imshow takes 2 arguments, 1: image title, 2: image var
cv2.imshow("study_pic", input)

# waitKey allows us to input information while the image window is open
# leaving it blank means, it waits for any key to be pressed before continuing
# placing a number will specify a DELAY (ms) for how long you keep the window open
cv2.waitKey()

# failure to run this will cause all programs to hang
cv2.destroyAllWindows()

# what's the dimension of the image?
print(input.shape) # height, width, number of components making up the image (RGB in this case)

# just to print output in a nice fashion
print("Image height: " , input.shape[0])
print("Image width: ", input.shape[1])

# opencv can store, save images in different formats
# imwrite takes 2 arguments, 1: file name, 2: image var
cv2.imwrite('output.jpg', input)





