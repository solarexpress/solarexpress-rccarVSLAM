# coding: utf-8 (for motor driver)
import time
import RPi.GPIO as GPIO
import cv2
from threading import Thread

dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)

# Use BOARD GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)

# for 1st Motor on ENA
ENA = 33
IN1 = 35
IN2 = 37
# for 2nd Motor on ENB
ENB = 36
IN3 = 38
IN4 = 40

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Enable
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)

# Forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)


# Define GPIO to use on Pi
GPIO_TRIGECHO = 15

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output


# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)

def camera():
  while True:
    ret, frame=cam.read()
    cv2.imshow('piCam',frame)
    if cv2.waitKey(1)==ord('q'):
      break   
def measure():
  global distance
  # This function measures a distance
  # Pulse the trigger/echo line to initiate a measurement
  GPIO.output(GPIO_TRIGECHO, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGECHO, False)
  #ensure start time is set in case of very quick return
  start = time.time()

  # set line to input to check for start of echo response
  GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
  while GPIO.input(GPIO_TRIGECHO)==0:
    start = time.time()

  # Wait for end of echo response
  while GPIO.input(GPIO_TRIGECHO)==1:
    stop = time.time()
  
  GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
  GPIO.output(GPIO_TRIGECHO, False)

  elapsed = stop-start
  distance = (elapsed * 34300)/2.0
  time.sleep(0.1)

try:
  while True:
    Thread(target=measure).start()
    Thread(target=camera).start()
    time.sleep(.1)
    if distance < 80:
      print("Object detected!")
      GPIO.output(ENA, GPIO.LOW)
      GPIO.output(ENB, GPIO.LOW)
      time.sleep(2)

      print("Reversing...")
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(ENB, GPIO.HIGH)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.HIGH)
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      time.sleep(.75)

      print("Moving out of the way.")
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(ENB, GPIO.HIGH)
      GPIO.output(IN1, GPIO.HIGH)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      time.sleep(.2)

    else:
      time.sleep(.5)
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(ENB, GPIO.HIGH)
      GPIO.output(IN1, GPIO.HIGH)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.HIGH)


except KeyboardInterrupt:
  print("Stop")
  GPIO.output(ENA, GPIO.LOW)
  GPIO.output(ENB, GPIO.LOW)
finally:
  GPIO.cleanup()
  cam.release()
  cv2.destroyAllWindows()
