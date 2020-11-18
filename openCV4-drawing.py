import cv2

print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#outVid=cv2.VideoWriter('videos/myCam3.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))

while True:
# read image
    ret, frame=cam.read()
# Draw Rectangle, position, color, thickness
    frame=cv2.rectangle(frame,(290,210),(350,270),(255,0,0),4)
# Draw Circle, position, radius, colar, thickness
    frame=cv2.circle(frame,(320,240),50,(255,50,100),4)
# Font variable - Text, position(First letter), var(fnt for this case),1=weight,color,thickness
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'My First Text', (250,350),fnt,1,(255,0,150),2)
# Line - Starting point, Ending point, color, thickness
    frame=cv2.line(frame, (10,10),(630,470),(0,0,0),4)
# Arrow Line - Same parameters of line
    frame=cv2.arrowedLine(frame,(10,450),(600,50),(0,0,200),4)
# show cam and moveWindow
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
# write video data of (frame)
    #outVid.write(frame)
# break out of video if (q) pressed
    if cv2.waitKey(1)==ord('q'):
        break        

cam.release()
#outVid.release()
cv2.destroyAllWindows()

    
   