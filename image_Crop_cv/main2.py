import numpy as np
import cv2

img = cv2.imread('image.jpg',0)
print(img.shape)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('saved.jpg',img)
    cv2.destroyAllWindows()
elif key in [27, 1048603]: # ESC key to abort, close window
    cv2.destroyAllWindows()
       