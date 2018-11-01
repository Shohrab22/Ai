import cv2
img = cv2.imread('image.jpg',0)
img1=img[:500,:500]
img2=img[:500,500:]
img3=img[500:,:500]
img4=img[500:,500:]
print(img.shape)
cv2.imshow('image',img)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.imshow('image4',img4)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('saved.jpg',img)
    cv2.destroyAllWindows()