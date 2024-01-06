import cv2

video = cv2.VideoCapture(0) # here 0 is used for desktop web came. by this code web cam will be opened

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