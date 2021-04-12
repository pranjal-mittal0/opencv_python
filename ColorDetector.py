import cv2
import numpy as np
#print("package imported")

#img=cv2.imread("Resources/img.png")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,-50)

def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue Max", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 179, 179, empty)
cv2.createTrackbar("Val Min", "HSV", 255, 255, empty)
cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)
while True:
    success,img=cap.read() #success is a boolean variable
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result=cv2.bitwise_and(img,img,mask= mask)
    #mask =cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    hstack=np.hstack((img,mask,result))
    cv2.imshow('Horizontal Stacking',hstack1)

    if (cv2.waitKey(30) & 0xFF) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()