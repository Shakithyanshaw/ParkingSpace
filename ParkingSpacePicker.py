import cv2
import pickle

img = cv2.imread('carParkImg.png')

while True:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) 