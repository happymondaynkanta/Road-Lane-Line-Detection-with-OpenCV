# detect_circles
import cv2
import numpy as np

img = cv2.imread('smarties.png')
#img = cv2.imread('shapes.jpg')

output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x,y), r, (50, 130, 255), 3)
    cv2.circle(output, (x,y), 3, (0, 255, 255), 3)

cv2.imshow("image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
