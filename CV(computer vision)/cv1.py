import cv2 # this library is used in AI, security, doctor line
im = cv2.imread(r'C:\Users\Priyanshu\Desktop\background.png') # reading the image/loading the image
if im is None: # this is to check none image
    print("not found")
else:
    print("image found")
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)# this is to change the image black and white
    im_inv = cv2.bitwise_not(im_gray) 
    im_rgb = cv2.cvtColor(im,cv2.COLOR_BGR2RGB) # this is to change the color of the image


    cv2.imshow('cosmere',im_gray) # this is to show the image on a pop screen
    cv2.imshow('cosmere_gray',im)
    cv2.imshow('cosmeer_inv',im_inv)
    cv2.imshow("cosmere_rgb",im_rgb)

    cv2.imwrite('CV(computer vision)/cosmere_gray.jpg',im_gray) # this is to save the image
    cv2.imwrite('CV(computer vision)/cosmere_inv.jpg',im_inv)
    cv2.imwrite('CV(computer vision)/cosmere_rgb.jpg',im_rgb)

    cv2.waitKey(0) # this is to hold the output screen until you not press any key


 