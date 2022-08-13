
import os
import cv2

path = "C:/Users/asus/Downloads/Pictures/Camera Roll"
image = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif',',jpeg', '.jpg', '.jfif', '.png']:
        
        file_name = path +"/"+ file
        image.append(file_name)
        print(file_name)

count = len(image)
print(count)
img = cv2.imread(image[0])
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
size = (width,height)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count):
     img = cv2.imread(image[i])
     print(image[i])
     out.write(img)

out.release()
print("Done")