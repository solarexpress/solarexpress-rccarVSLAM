import cv2
import numpy as np
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#outVid=cv2.VideoWriter('videos/myCam3.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))

# For webCam - get frame width and height form cam.get
#dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
#dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Box Width & Height - Start position and change of xy for box
BW=96
BH=96
BW2=96
BH2=96

posX=10
posY=270
posX2=300
posY2=250
dx=6
dy=6
dx2=6
dy2=6

#    tBox1=np.array((posX,posY),(posX+BW,posY),1)  
#    lBox1=np.array((posX,posY),(posX,posY+BH),1)
#    rBox1=np.array((posX+BW,posY),(posX+BW,posY+BH),1)
#    bBox1=np.array((posX,posY+BH),(posX+BW,posY+BH),1)
# 
#    tBox2=np.array((posX2,posY2),(posX2+BW2,posY2),1)
#    lBox2=np.array((posX2,posY2),(posX2,posY2+BH2),1) 
#    rBox2=np.array((posX2+BW2,posY2),(posX2+BW2,posY2+BH2),1)
#    bBox2=np.array((posX2,posY2+BH2),(posX2+BW2,posY2+BH2),1)


while True:
# read image
    ret, frame=cam.read()
# Draw Rectangle, position, color, thickness
    #frame=cv2.rectangle(frame,(290,210),(350,270),(255,0,0),4)
# Draw Circle, position, radius, colar, thickness
    #frame=cv2.circle(frame,(320,240),50,(255,50,100),4)
# Font variable - Text, position(First letter), var(fnt for this case),1=weight,color,thickness
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'SolarExpress', (250,350),fnt,1,(255,0,150),2)
# Messing with axis equal to each other to display a comment in frame
    fnt=cv2.FONT_HERSHEY_DUPLEX
    if posX==posX2 or posY==posY2:
        ifAxis=cv2.putText(frame, 'The Axis Matched', (250,100),fnt,1,(255,100,50),2)
# cv2.rectangle of frame - (start pos),(next pos/ending pos),(color)
    frame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,150),-1)
    frame=cv2.rectangle(frame,(posX2,posY2),(posX2+BW2,posY2+BH2),(155,100,50),-1)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    
# if statement to contain box in (frame), the dispW*dispH
    posX=posX+dx
    posY=posY+dy
    if posX<=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<=0 or posY+BH>dispH:
        dy=dy*(-1)

    posX2=posX2+dx2
    posY2=posY2+dy2
    if posX2<=0 or posX2+BW2>=dispW:
        dx2=dx2*(-1)
    if posY2<=0 or posY2+BH2>dispH:
        dy2=dy2*(-1)
    
    if posX+BW==posX2:
        dx=dx*(-1)
        dx2=dx2*(-1)
    if posY+BH==posY2:
        dy=dy*(-1)
        dy2=dy2*(-1)
    

    lt1=(posX,posY)
    rt1=(posX+BW,posY)
    tBox1=[lt1,rt1] 
    t1=tBox1.append(tBox1)
    #lt1=(posX,posY)
    lb1=(posX,posY+BH)
    lBox1=[lt1,lb1]
    l1=lBox1.append(lBox1)
    #rt1=(posX+BW,posY)
    rb1=(posX+BW,posY+BH)
    rBox1=[rt1,rb1]
    r1=rBox1.append(rBox1)
    #lb1=(posX,posY+BH)
    #rb1=(posX+BW,posY+BH)
    bBox1=[lb1,rb1]
    b1=bBox1.append(bBox1)

    lt2=(posX2,posY2)
    rt2=(posX2+BW2,posY2)
    tBox2=[lt2,rt2] 
    t2=tBox2.append(tBox2)
    #lt2=(posX2,posY2)
    lb2=(posX2,posY2+BH2)
    lBox2=[lt2,lb2]
    l2=lBox2.append(lBox2)
    #rt2=(posX2+BW2,posY2)
    rb2=(posX2+BW2,posY2+BH2)
    rBox2=[rt2,rb2]
    r2=rBox2.append(rBox2)
    #lb2=(posX2,posY2+BH2)
    #rb2=(posX2+BW2,posY2+BH2)
    bBox2=[lb2,rb2]
    b2=bBox2.append(bBox2)
     
    cond1=np.any(t1)
    cond11=np.any(b2)
    cond2=np.any(r1)
    cond21=np.any(l2)
    cond3=np.any(b1)
    cond31=np.any(t2)
    cond4=np.any(l1)
    cond41=np.any(r2)
    
    
    if cond1==cond11:
        dy=dy*(-1)
        dy2=dy2*(-1)
    if cond2==cond21:
        dx=dx*(-1)
        dx2=dx2*(-1)
    if cond3==cond31:
        dy=dy*(-1)
        dy2=dy2*(-1)
    if cond4==cond41:
        dx=dx*(-1)
        dx2=dx2*(-1) 
        


    #if posX+BW>=posY2 or posX+BW<=posY2+BH2 and posX+BW==posX2:
     #   dx=dx*(-1)
      #  dx2=dx2*(-1)

   

    breakKey=cv2.waitKey(1)
    if breakKey==ord('q'):
        break  
    

cam.release()
#outVid.release()
cv2.destroyAllWindows()

    
   