import cv2
#print("package imported")
framewidth=640
frameheight=480

#img=cv2.imread("Resources/img.png")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,-50)

myColors=[]

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("img",mask)
while True:
    success,img=cap.read() #success is a boolean variable
    cv2.imshow("Video",img)
    if (cv2.waitKey(30) & 0xFF) == ord("q"):
        break
