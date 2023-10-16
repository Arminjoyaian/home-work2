import cv2
image = cv2.imread(r"c:\Users\Lenovo\Downloads\IMG_20230914_153023_665.JPG")
image = cv2.resize(image, (300,500))
image = cv2.rectangle(image, (125,125),(175,175),(125,0,0))
cv2.imshow('My',image)
cv2.waitKey(0)
image= cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
cv2.imwrite(r"c:\Users\Lenovo\Pictures\photo.img" , image)
