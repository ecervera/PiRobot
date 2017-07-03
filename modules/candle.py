import numpy as np
import cv2
import sys

def candle(img, lower=150, upper=255):
    region = img[250:,:,:]
    lower_tuple = (lower,lower,lower)
    upper_tuple = (upper,upper,upper)
    mask = cv2.inRange(region, lower_tuple, upper_tuple)
    cnt, hrc = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if cnt:
        cnt.sort(key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect( np.vstack(tuple(cnt)) )
        if w>1 and h>1:
            x += w/2
            y += h/2
            return x, y, w, h
        else:
            return None, None, None, None
    else:
        return None, None, None, None
