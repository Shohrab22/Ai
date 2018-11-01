import cv2
img = cv2.imread('img.jpg',-1)
img_h,img_w,_=img.shape
img_h_mid=img_h//2
img_w_mid=img_w//2
cv2.line(img,(img_w_mid,0),(img_w_mid,img_h),(0,0,255),5)
cv2.line(img,(0,img_h_mid),(img_w,img_h_mid),(0,0,255),5)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('saved.jpg',img)
    cv2.destroyAllWindows()