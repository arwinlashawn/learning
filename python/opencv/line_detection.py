import cv2
import numpy as np 
import os 


### WARNING: this program is not working properly. Keep getting unexpected output

os.chdir("/Users/macintosh/Desktop")

# load the image
image = cv2.imread("sudoku.png")

# grayscale and use canny to extract edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# run HoughLines using a rho accuracy of 1 pixel
# theta accuracy of np.pi / 180 which is 1 degree
# our line threshold is set to 240 (number of points on line)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)

# we iterate through each line and convert it to the format
# required by cv.lines (i.e. requiring end points)
for rho, theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * rho
	y0 = b * rho
	x1 = int(x0 + 1000 * (-b))
	y1 = int(y0 + 1000 * (a))
	x2 = int(x0 - 1000 * (-b))
	y2 = int(y0 - 1000 * (a))
	cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

cv2.imshow("Hough Lines", image)
cv2.waitKey()
cv2.destroyAllWindows()


### Probabilistic Hough Lines

# grayscale and extract edges using canny
image = cv2.imread("sudoku.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize=3)

# again we use the same rho and theta accuracies
# however, we specify a minimum vote (points along line) of 100
# and minimum line length of 5 pixels and max gap between lines of 10 pixels
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 2, 80)
print(lines.shape)

for x1, y1, x2, y2 in lines[0]:
	cv2.line(image, (x1, x2), (y1, y2), (0, 255, 0), 3)

cv2.imshow("Probabilistic Hough Lines", image)
cv2.waitKey()
cv2.destroyAllWindows()







