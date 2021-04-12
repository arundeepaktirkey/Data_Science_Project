# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:01:22 2021

@author: asus
"""

import cv2
import os

def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)

    cap = cv2.VideoCapture(pathIn)
    count = 0

    while (cap.isOpened()):
        print("1")
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    extractFrames('E:/IVY/ML with PYTHON/Materials/DEEP LEARNING/Lane Detection/test2.mp4', 'E:/IVY/ML with PYTHON/Materials/DEEP LEARNING/Lane Detection/test2_frames')

if __name__=="__main__":
    main()