from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # with draw
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)
        if fingers1[1] == 1 and fingers1[2] == 1:
            length, info, img = detector.findDistance(lmList1[8], lmList1[12], img)
            pyautogui.click()
        elif fingers1[1] == 1 and fingers1[2] == 0:
            x, y = lmList1[8]
            xo = np.interp(x, [135, 1186], [0, 1920])
            yo = np.interp(y, [80, 572], [0, 1080])
            print(lmList1[8])
            pyautogui.moveTo(1920 - xo, yo)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)