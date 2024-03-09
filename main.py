import threading
import cv2 as cv
from deepface import DeepFace

      
cap = cv.VideoCapture(0, cv.CAP_DSHOW) #open cv video capture object (0 refernces the first - and only camera - on my laptop, CAP_DSHOW specifies the video source for windows) 

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640) #width and height of displayed video fram
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 280)

