import cv2
import numpy as np
hand= cv2.imread('Capture.png',0)
ret, the=cv2.threshold(hand, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Original Image',hand)
cv2.waitKey(0)
cv2.destroyAllWindows()