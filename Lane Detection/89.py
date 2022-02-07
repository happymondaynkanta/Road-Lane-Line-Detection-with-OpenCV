# line detector - set a piece of an image as 'region of interest' (ROI)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.png')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


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
    channel_count = img.shape[2]
    match_mask_color = (255, ) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image



cropped_image = region_of_interest(img,
    np.array([region_of_interest_vertices], np.int32),)



plt.imshow(cropped_image)
plt.show()
