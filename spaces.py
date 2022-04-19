import cv2 as cv
img=cv.imread("G:\learn opencv/DIP.jpg") #by default opencv will read image in BGR format 
cv.imshow("original image", img)
#BGR to gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#BGR to HSV
hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv space",hsv_img)
cv.waitKey(0)