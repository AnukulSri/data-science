import cv2

video = cv2.VideoCapture(r'E:\REC.VDO-ARJUN\00093.MTS')

while video.isOpened():
    status, img = video.read()
    if status:
         cv2.imshow('video',img)

         if cv2.waitKey(1) ==27: # 27 is for esc key
            break
         else:
            print('video ended')
            break
video.release()
cv2.destroyAllWindows