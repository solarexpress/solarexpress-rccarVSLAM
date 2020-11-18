import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
piCam=cv2.VideoCapture(camSet)
webCam=cv2.VideoCapture(1,200)
webCam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame=piCam.read()
    ret, frame2=webCam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    #cv2.imshow('piCam2',frame)
    #cv2.moveWindow('piCam2',5200,0)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayPiCam',gray)
    cv2.moveWindow('grayPiCam',400,0)
    #cv2.imshow('grayPiCam2',gray)
    #cv2.moveWindow('grayPiCam2',700,520)

    cv2.imshow('webCam',frame2)
    cv2.moveWindow('webCam',0,300)
    cv2.imshow('graywebCam',gray2)
    cv2.moveWindow('graywebCam',400,300)    
    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()        
piCam.release()
cv2.destroyAllWindows()
