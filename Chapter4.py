import cv2
import numpy as np
#img=np.zeros((512,512)) #greyscale
img=np.zeros((512,512,3),np.uint8)#gives color img  and np.unit8 gives 255 colors (hight, width, channel
#print(img.shape) #it gives just the tuple or better say dimentions
#img[:]=0,20,0 #BGR  img[200:400,400:600] gives that particular section [width, hight]
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,50,150),4)
cv2.circle(img,(450,150),50,(20,158,23),3)
cv2.putText(img,"opencv chapter4",(100,500),cv2.FONT_HERSHEY_SIMPLEX,1,(150,0,34),3)
cv2.imshow("image", img)

cv2.waitKey(4000)