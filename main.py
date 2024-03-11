import threading
import cv2 as cv
from deepface import DeepFace # https://github.com/serengil/deepface

      
cap = cv.VideoCapture(0, cv.CAP_DSHOW) #(0 refernces the first - and only camera - on my laptop, CAP_DSHOW specifies the video source for windows) 

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640) #width and height of displayed video fram
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 280)

timer = 0 #run every 25 seconds
face_match = False
ref_img = cv.imread("myface.jpg") #loads my face image

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, ref_img.copy())['verified']: #copied ref_img passed to avoid manipulation to the original photo
            face_match = True
        else:
            face_match = False
    except ValueError: #face isn't recognized
        face_match = False

while True:
    can_read, next_frame = cap.read() # cap.read() returns a boolean and the next frame of video 

    if can_read:
        if timer % 25 == 0:
            pass
            '''
            try:
                threading.Thread(target=check_face, args=(next_frame.copy(),)).start() #copy of the frame is passed unto check_face to 
            except ValueError: #deepface returns a value error when there isn't a match (strange)
                pass
'''
        timer += 1

        if face_match:
            next_frame_wtext = cv.putText(next_frame, "VERIFIED", (20, 450), cv.FONT_ITALIC, 2, (0, 255, 0), 3) #displays veried if there's a match and not verified otherwise
        else:
            next_frame_wtext = cv.putText(next_frame, "NOT VERIFIED", (20, 450), cv.FONT_ITALIC, 2, (0, 0, 255), 3)

        cv.imshow("video frame", next_frame_wtext) # displays video stream


    key = cv.waitKey(1) #quit when q is pressed
    if key == ord('q'):
        break

cv.destroyAllWindows() #end cv stream

