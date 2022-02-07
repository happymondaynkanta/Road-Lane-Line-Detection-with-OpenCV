# line detector - set a piece of an image as 'region of interest' (ROI)
import cv2
import numpy as np
from matplotlib import pyplot as plt


# mask other part of the image thats not on the area you specified

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype= np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0,255,0), 4)


    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)

    return img






def process(img):

    #print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # get an area of the image

    region_of_interest_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]



    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny_image = cv2.Canny(gray_image, 100, 200)



    cropped_image = region_of_interest(canny_image,
        np.array([region_of_interest_vertices], np.int32),)



    lines = cv2.HoughLinesP(cropped_image, rho=6,
            theta=np.pi /60, threshold=160, lines=np.array([]),
            minLineLength=40, maxLineGap=25)


    image_with_lines = draw_the_lines(img, lines)

    return image_with_lines




cap = cv2.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
