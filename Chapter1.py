import cv2
print("package imported")

#img=cv2.imread("Resources/img.png")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,-50)
while True:
    success,img=cap.read() #success is a boolean variable
    cv2.imshow("Video",img)
    if (cv2.waitKey(30) & 0xFF) == ord("q"):
        break
