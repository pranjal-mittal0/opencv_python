import cv2
import numpy as np
img=cv2.imread("Resources/cards.jpg")

width,height=250,350 #aspect ratio of playing card is 2.5 to 3.5
pts1= np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)
imgOutput= cv2.warpPerspective(img,matrix,(width, height))


#pts1=np.float32()
cv2.imshow("IMG", imgOutput)
cv2.waitKey(3000)
