#!/usr/bin/env python

import math

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("3 (copy).jpeg", 1)
    
    cv2.putText(img=img, text="Hello", org=(500, 500), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.putText(img, "Hello", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 0, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey(0)
