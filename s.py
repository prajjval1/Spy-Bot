import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

cascade = cv2.CascadeClassifier('/home/pi/Downloads/haarcascade_fullbody.xml')

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera,size=(640,480))

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
	img = frame.array
	img = cv2.flip(img,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	human = cascade.detectMultiScale(gray,1.01,8)
	for (x,y,w,h) in human:
		cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,0,255),2)
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		rawCapture.truncate(0)

cap.release()
cv2.destroyAllWindows()
