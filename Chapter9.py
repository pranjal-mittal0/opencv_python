import cv2

faceCascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,-50)
while True:
    success,img=cap.read() #success is a boolean variable
#     cv2.imshow("Video",img)
# img=cv2.imread('Resources/lena.png')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)

    cv2.imshow("Image", img)
    if (cv2.waitKey(30) & 0xFF) == ord("q"):
        break