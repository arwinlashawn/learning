import cv2
import numpy as np 
import os 

os.chdir("/Users/macintosh/Desktop")

# we point OpenCV's CascadeClassifier function to where our
# classifier (XML file format) is stored
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# load the image
image = cv2.imread("uwppic.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# our classifier returns the ROI of the detected face as a tuple
# it stores the top left coordinate and the bottom right coordinate
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# when no face is detected, face_classfier returns an empty tuple
if faces is ():
	print("No face found")

# we iterate through our face array and draw a rectangle
for (x,y,w,h) in faces:
	cv2.rectangle(image, (x,y), (x + w, y + h), (127, 0, 255), 2)
	cv2.imshow("Face Detected", image)
	cv2.waitKey()


cv2.destroyAllWindows()

