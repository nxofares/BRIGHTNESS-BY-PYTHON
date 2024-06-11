import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands= mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    succes,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    ImList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for if,lm in enumerate(handlandmark.landmark):
                h,w,_ = img.shape
            cx,cy = int(lm.x*w),int(lm.y*h)
            