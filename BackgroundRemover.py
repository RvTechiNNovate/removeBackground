import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import numpy as np

# image path
path="view1.jpeg"

# background image
img = cv2.imread("BackgroundImages\\1.jpg")


segmentor = SelfiSegmentation()

listImg = os.listdir("BackgroundImages")
imgList = []


imgbg = cv2.resize(img, (403,302))


indexImg=3


img=cv2.imread(path)
img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)
print(img.shape)

imgOut = segmentor.removeBG(img, imgbg , threshold=0.0000012)


imgStack = np.hstack((img, imgOut))




cv2.imshow("output", imgOut)
cv2.waitKey(5000)

