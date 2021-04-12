import cv2
import numpy as np
img=cv2.imread("Resources/img.png")
kernel= np.ones((5,5), np.uint8)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur =cv2.GaussianBlur(imggray,(5,5),0)
imgCanny=cv2.Canny(img,200,150)
imgdialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgeroded=cv2.erode(imgdialation,kernel,iterations=1)



cv2.imshow("Gray Image", imggray)
cv2.imshow("blur Image", imgblur)
cv2.imshow("canny Image", imgCanny)
cv2.imshow("Dialation Image", imgdialation)
cv2.imshow("erosion Image", imgeroded)


cv2.waitKey((5000))