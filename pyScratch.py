import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#piCam=cv2.VideoCapture(camSet)
webCam=cv2.VideoCapture(1,200)

while True:
    #ret, frame=piCam.read()
    ret, frame2=webCam.read()
    #cv2.imshow('Raspberry Pi Cam',frame)
    cv2.imshow('C290 Logitech WebCam',frame2)
    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()        
#cam.release()
cv2.destroyAllWindows()
