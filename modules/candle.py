import numpy as np
import cv2
import sys

def maxArea(contours):
    imax = 0
    x,y,w,h = cv2.boundingRect(contours[0])
    maxA = w*h
    i = 1
    lc = len(contours)
    while i<lc:
        x,y,w,h = cv2.boundingRect(contours[i])
        if w*h > maxA:
            maxA = w*h
            imax = i
        i = i + 1
    return imax

def findBlob(img,lower,upper):
    mask = cv2.inRange(img, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    lc = len(contours)
    if lc>0:
        found = True
        imax = maxArea(contours)
        maxCnt = contours[imax]
        x,y,w,h = cv2.boundingRect(maxCnt)
    else:
        found = False
        x,y,w,h = 0,0,0,0
    return found,x,y,w,h
       
def state(img,x,y,w,h):
    roi = img[y-h:y, x:x+w, :]
    whiteLower = (240,240,240)
    whiteUpper = (255,255,255)
    found,x,y,w,h = findBlob(roi,whiteLower,whiteUpper)
    if not found:
        return False
    else:
        if float(h)/w > 0.25:
            return True
        else:
            return False
        
def position(img):
    # bgr
	#redLower = ( 0,  0, 100)
    #redUpper = (50, 50, 255)
    # rgb
    redLower = (100,  0,  0)
    redUpper = (255, 50, 50)
    found,x,y,w,h = findBlob(img,redLower,redUpper)
    return found,x,y,w,h

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: candle.py filename")
        sys.exit()
    img = cv2.imread(sys.argv[1])
    found,x,y,w,h = position(img)
    if found:
        print('Candle bounding box: (x,y)=(%d,%d), w=%d, h=%d ' % (x,y,w,h))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        lit = state(img,x,y,w,h)
        if lit:
            print('It seems to be ON')
        else:
            print('It seems to be OFF')
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('No candle found in image')
    