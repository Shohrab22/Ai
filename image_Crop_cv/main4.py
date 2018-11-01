import cv2
img = cv2.imread('image.jpg',0)
cv2.line(img,(0,0),(511,511),(0,0,255),5)
cv2.imshow('image',img) 
k = cv2.waitkey(0)  
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('saved.jpg',img) 
    cv2.destroyAllWindows()