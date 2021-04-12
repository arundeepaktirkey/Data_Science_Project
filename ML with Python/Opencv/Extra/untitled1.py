# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:19:59 2021

@author: asus
"""

import cv2
import time

cap = cv2.VideoCapture("E:/IVY/ML with PYTHON/Materials/DEEP LEARNING/Lane Detection/video.mp4")


fps= int(cap.get(cv2.CAP_PROP_FPS))

print("This is the fps ", fps)

if cap.isOpened() == False:
    print("Error File Not Found")

while (cap.isOpened()):
    print("1")
    ret,frame= cap.read()
    print("2")
    if ret == True:
        print("3")
        time.sleep(1/fps)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()
