import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2

# Define 'nothing' function
def nothing(x):
    pass

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)

# Introduce Window and Trackbar-(0, not start value its the initial setting on trackbar)
cv2.namedWindow('piCam')
cv2.createTrackbar('xVal','piCam',25,dispW,nothing)
cv2.createTrackbar('yVal','piCam',25,dispH,nothing)
cv2.createTrackbar('Width','piCam',25,dispW,nothing)
cv2.createTrackbar('Height','piCam',25,dispH,nothing)
cv2.FOn
while True:
    ret, frame=cam.read()
    
    # Reading Trackbar (x value and y value)
    xVal=cv2.getTrackbarPos('xVal','piCam')
    yVal=cv2.getTrackbarPos('yVal','piCam')
    Width=cv2.getTrackbarPos('Width','piCam')
    Height=cv2.getTrackbarPos('Height','piCam')
    
    # Use trackbar to place circle
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
    innerCircle=cv2.circle(frame,(Width,Height),4,(255,0,200),1)
    cv2.rectangle(frame,(xVal-20,yVal-20),(xVal+Width,yVal+Height),(255,0,200),2)
    cv2.rectangle(innerCircle,(Width,Height),(Width,Height),(255,0,200),2)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break        
cam.release()
cv2.destroyAllWindows()

    
  # /home/solarexpress/Desktop/pyPro/openCV/openCV7-trackBar.py
