import cv2
img = cv2.imread('image.jpg',0)

part=4
img_h,img_w=img.shape
start_point=0
part_w=int(img_w/part)
part_h=int(img_h/part)
for i in range(part):
    end_point=start_point+part_w
   
    
    start_point2=0
    for j in range(part):
         end_point2=start_point2+part_h
         print(str(start_point)+" : "+str(end_point)+
              " - "+str(start_point2)+" : "+str(end_point2))
         img1=img[start_point:end_point,start_point2:end_point2]
         cv2.imwrite(str(i)+"_"+str(j)+'.jpg',img1)
         start_point2= end_point2
    start_point= end_point        
    print("-------------------------------------")
    
    