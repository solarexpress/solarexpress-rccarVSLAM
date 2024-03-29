import cv2
print(cv2.__version__)
import numpy as np
import threading
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
pan=90

kit.servo[0].angle=pan
kit.servo[1].angle=10
def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueLower', 'Trackbars',21,179,nothing)
cv2.createTrackbar('hueUpper', 'Trackbars',65,179,nothing)

cv2.createTrackbar('hue2Lower', 'Trackbars',50,179,nothing)
cv2.createTrackbar('hue2Upper', 'Trackbars',0,179,nothing)

cv2.createTrackbar('satLow', 'Trackbars',86,255,nothing)
cv2.createTrackbar('satHigh', 'Trackbars',211,255,nothing)
cv2.createTrackbar('valLow','Trackbars',122,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',206,255,nothing)

objArea = 0

def Trackbars():
    hueLow=cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp=cv2.getTrackbarPos('hueUpper', 'Trackbars')

    hue2Low=cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    hue2Up=cv2.getTrackbarPos('hue2Upper', 'Trackbars')

    Ls=cv2.getTrackbarPos('satLow', 'Trackbars')
    Us=cv2.getTrackbarPos('satHigh', 'Trackbars')

    Lv=cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv=cv2.getTrackbarPos('valHigh', 'Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    l_b2=np.array([hue2Low,Ls,Lv])
    u_b2=np.array([hue2Up,Us,Uv])   

def Tracking():
    contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=100:
            if cv2.waitKey(1)==ord('c'):
                objArea = area
                print("Object area captured as", objArea)

            cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            objX=x+w/2
            objY=y+h/2
            errorPan=objX-width/2

            if area < 0.3*objArea:
                kit.servo[1].angle=105
            
            if area > objArea:
                kit.servo[1].angle=10

            if abs(errorPan)>15:
                pan=pan+errorPan/25

            if pan>150:
                pan=150
                
            if pan<55:
                pan=55
                #print("Pan Out of  Range") 

            kit.servo[0].angle=pan
  
            break  

def ShowWindows():
    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,530) 
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)  

dispW=640
dispH=480
flip=2
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(1)
width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('width:',width,'height:',height)
while True:
    ret, frame = cam.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    threading.start_new_thread(Trackbars, ())
    threading.start_new_thread(Tracking, ())
    threading.start_new_thread(ShowWindows())


    if cv2.waitKey(1)==ord('q'):
        break
        kit.servo[1].angle=10
cam.release()
cv2.destroyAllWindows()
