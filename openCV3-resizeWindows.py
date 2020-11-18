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
# Setting up the Frame for piCam and webCam
    ret, frame=piCam.read()
    ret, frame2=webCam.read() 
# piCam grayscale setup - piCam resize and grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameSmall=cv2.resize(frame,(160,120))
    graySmall=cv2.resize(gray,(160,120))
# piCam - grayPiCam
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    cv2.imshow('grayPiCam',gray)
    cv2.moveWindow('grayPiCam',400,0)
# Resized piCam - Resized piCamSmallgray (2 Frames)
    cv2.imshow('piCamSmallgray',graySmall)
    cv2.moveWindow('piCamSmallgray',730,0)
    cv2.imshow('piCamSmall',frameSmall)
    cv2.moveWindow('piCamSmall',730,160)

# webCam grayscale setup - webCam resize and grayscale 
    gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    frameSmall2=cv2.resize(frame2,(160,120))
    graySmall2=cv2.resize(gray2,(160,120))
# webCam - graywebCam (2 Frames)
    cv2.imshow('webCam',frame2)
    cv2.moveWindow('webCam',0,300)
    cv2.imshow('graywebCam',gray2)
    cv2.moveWindow('graywebCam',400,300)    
# Resized webCam - Resized webCam BW (2 Frames) 
    cv2.imshow('grayWebCamSmall',graySmall2)
    cv2.moveWindow('grayWebCamSmall',730,300)
    cv2.imshow('webCamSmall',frameSmall2)
    cv2.moveWindow('webCamSmall',730,460)

    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()        
piCam.release()
cv2.destroyAllWindows()
