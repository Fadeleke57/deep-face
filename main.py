import threading #parallel processing 
import cv2 as cv
from deepface import DeepFace #might need to downgrade tensorflow to 2.12 bc LocallyConnected2D layer is no longer available in TensorFlow 2.x Keras API. https://stackoverflow.com/questions/78131429/importerror-cannot-import-name-locallyconnected2d-from-tensorflow-keras-laye/78131539#78131539

      
cap = cv.VideoCapture(0, cv.CAP_DSHOW) #open cv video capture object (0 refernces the first - and only camera - on my laptop, CAP_DSHOW specifies the video source for windows) 

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640) #width and height of displayed video fram
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 280)

timer = 0 #run every 25 seconds

face_match = False

ref_img = cv.imread("myface.jpg") #loads my face image

while True:
    can_read, next_frame = cap.read() # cap.read() returns boolean, then the next frame of video 

    if can_read:
        continue

    key = cv.waitKey(1) #quit when q is pressed
    if key == ord('q'):
        break

cv.destroyAllWindows() #end cv stream

