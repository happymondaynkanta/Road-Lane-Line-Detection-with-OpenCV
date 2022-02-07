# line detector - set a piece of an image as 'region of interest' (ROI)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


print(img.shape)
height = img.shape[0]
width = img.shape[1]

# get an area of the image

region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]


# mask other part of the image thats not on the area you specified

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image



gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(gray_image, 100, 200)


cropped_image = region_of_interest(canny_image,
    np.array([region_of_interest_vertices], np.int32),)


plt.imshow(cropped_image)
plt.show()
