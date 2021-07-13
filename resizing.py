import cv2

img = cv2.imread('BackgroundImages/2.jpg')
img = cv2.resize(img, (403,302))
# 302,403
# cv2.imshow("img", img)
# cv2.waitKey(0)
cv2.imwrite("5.jpg", img)