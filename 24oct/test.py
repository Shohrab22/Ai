import cv2 as cv

img = cv.imread('img.jpg',cv.IMREAD_GRAYSCALE)
print(img.shape)
#cv.imshow('image',img)

part = 20
imgWidth = 1000
startPoint = 0
partWidth = int(1000/20)
for i in range(part):
	endPoint = startPoint + partWidth
	print(str(startPoint)+" : "+str(endPoint))
	startPoint = endPoint
	
#cv.destroyAllWindows()

'''
k = cv.waitKey(0)

if k==27:
	cv.destroyAllWindows()
elif k==ord('s'):
	#cv.imwrite('saved.jpg', img)
	img1 = img[:500, :500]
	img2 = img[:500, 500:1000]
	img3 = img[500:, :500]
	img4 = img[500:, 500:]
	cv.imwrite('img1.jpg', img1)
	cv.imwrite('img2.jpg', img2)
	cv.imwrite('img3.jpg', img3)
	cv.imwrite('img4.jpg', img4)
	cv.destroyAllWindows()
'''