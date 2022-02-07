# Road-Lane-Line-Detection-with-OpenCV
Using computer vision techniques in OpenCV, we will identify road lane lines in which autonomous cars must run. This will be a critical part of autonomous cars, as the self-driving cars should not cross it’s lane and should not go in opposite lane to avoid accidents.

## Frame Masking and Hough Line Transformation

To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using frame masking. The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we simply update those pixel values to 0 in the NumPy array.



