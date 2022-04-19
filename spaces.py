import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
img=cv.imread("G:\learn opencv/DIP.jpg") #by default opencv will read image in BGR format 
cv.imshow("original image", img)
#BGR to gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#BGR to HSV
hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)  # the inversion is cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow("hsv space",hsv_img)
#BGR to LAB
lab_img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB space",lab_img)
#BGR to RGB
rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB space",rgb_img)
#check matplotlib
plt.imshow(img) #plt reads pictures by RGB and cause img is provided by cv2 and it's in BGR form,
#when plt reads it, color inversion will occur R-->B and vice versa 
plt.show()
#split colors
b,g,r=cv.split(img)
cv.imshow("blue channel",b) #show intesity of blue in original image, so it's gray 
cv.imshow("green channel",g)
cv.imshow("red channel",r)
#merge colors 
merged_img=cv.merge([b,g,r])
cv.imshow("merged image",merged_img)
#blue image 
blank=np.zeros(img.shape[:2],dtype="uint8")
bluish_img=cv.merge([b,blank,blank])
cv.imshow("bluish",bluish_img)
cv.waitKey(0)