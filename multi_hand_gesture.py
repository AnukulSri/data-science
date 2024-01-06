import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

tipIds = [4,8,12,16,20] 
#tipIds2 = [4,8,12,16,20]
state = None
Gesture = None
wcam,hcam = 720,640

def fingerPosition (image,handNo = 0):
    lmlist = []
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id,lm in enumerate(myHand.landmark):
            h,w,c = image.shape
            cx, cy = int(lm.x*w),int(lm.y*h)
            lmlist.append([id,cx,cy])
    return lmlist

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame")
            continue
        image =  cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
                lmList = fingerPosition(image)
                if len(lmList)!=0:
                    fingers=[]
                    for id in range(1,5):
                         if  lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                            fingers.append(0)
                         else:   
                            fingers.append(1)
                    totalFingers = fingers.count(0)
                    print(totalFingers)
                   # print(lmList[9][2])


                    if totalFingers == 4:
                        state="Play"
                    if totalFingers ==0 and state == "Play":
                        state= "Pause"
                        pyautogui.press('space')
                        print('Space')
                    if totalFingers ==1:
                        if lmList[8][1]<300:
                            print("left")
                            pyautogui.press('left')
                        if lmList[8][1]>400:
                            print("Right")
                            pyautogui.press('Right')
                    if totalFingers ==2:
                        if lmList[9][2]<210:
                            print("Up")
                            pyautogui.press('volumeup')
                        if lmList[9][2]>230:
                            print("Down")
                            pyautogui.press('volumedown')

                cv2.imshow("Media Controller",image)
                #key = cv2.waitKey(1) &0xFF
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()                
cv2.destroyAllWindows()