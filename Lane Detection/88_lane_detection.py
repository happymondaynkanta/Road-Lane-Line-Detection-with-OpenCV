# line detector

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.png')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)
height = img.shape[0]
width = img.shape[1]

plt.imshow(img)
plt.show()
