import cv2

im = cv2.imread(r'C:\Users\Priyanshu\Desktop\pikachu.jpg')


if im is None:
    print("image not found")
h,w,_ = im.shape
small_im = cv2.resize(im,(w//2,h//2))

bright_im= cv2.add(im,50)
light_im= cv2.add(im,-50)

flip_im = cv2.flip(im,0)

stitched_h_im = cv2.hconcat(im,flip_im)
stitched_V_im = cv2.vconcat(im, flip_im)


cv2.imshow('original',im)
cv2.imshow('resize',small_im)
cv2.imshow('dark',bright_im)
cv2.imshow('light',light_im)
cv2.imshow('flip',flip_im)
cv2.imshow('stiched_h',stitched_h_im)
cv2.imshow('stiched_v',stitched_V_im)

cv2.waitKey(0)

