import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(imgContour):
    contours,hierarchy = cv2.findContours(imgContour,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        if area >500: #pixels
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter=cv2.arcLength(cnt,True)
            #print(perimeter)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True) #corners
            objCorner=len(approx)
            x,y,width,height=cv2.boundingRect((approx))

            cv2.rectangle(imgContour,(x,y),(x+ width,y+ height),(0,0,255),2)
            if objCorner==3:
                ObjectType="Triangle"
            else:
                ObjectType="none"
            cv2.putText(imgContour,ObjectType,((x+(width/2)-10),y+(height/2)-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,222),2)

path="Resources/shapes.png"
img=cv2.imread(path)
imgContour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank=np.zeros_like(img)
imgStack=stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))
cv2.imshow("Stack",imgStack)
cv2.waitKey(0)






