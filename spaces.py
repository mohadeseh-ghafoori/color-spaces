from colorsys import rgb_to_hls
import cv2 as cv
img=cv.imread("G:\learn opencv/DIP.jpg") #by default opencv will read image in BGR format 
cv.imshow("original image", img)
#BGR to gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#BGR to HSV
hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv space",hsv_img)
#BGR to LAB
lab_img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB space",lab_img)
#BGR to RGB
rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB space",rgb_img)
cv.waitKey(0)