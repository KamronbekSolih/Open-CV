from sre_constants import SUCCESS
import cv2
import numpy as np
# print("Success")
# img=cv2.imread("media/fw.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)            #Outputs an image

# capture=cv2.VideoCapture(1)
# capture.set(3,3840) #defines width
# capture.set(4,600)
# capture.set(10,300)
# while True:
#     SUCCESS, img=capture.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('k'):
#         break         #Video capture

#Chapter 2
img=cv2.imread("D:/Python/Open CV/media/uzmobile.png")

karnel=np.ones((7,7),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(img,(11,11),0)
imgCanny = cv2.Canny(img,500, 700, apertureSize = 5, L2gradient = True)
imgDial=cv2.dilate(imgCanny, karnel, iterations=1)
imgEroded= cv2.erode(imgDial,karnel, iterations=1 )

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDial)
cv2.imshow("Eroded Image", imgEroded)

cv2.imwrite('D:/Python/Open CV/media/uzmobile_canny.png',imgCanny)
   
cv2.waitKey(0)

# img=cv2.imread("media/cat.jpg")
# #print(img.shape)  getting the size of the image
# imgResize = cv2.resize(img,(700,600)) # Resizing
# imgCropped= img[50:700,300:600]
# # cv2.imshow("Rasm",img)
# cv2.imshow("Resized rasm",imgResize)
# cv2.imshow("Cropped rasm",imgCropped)
# cv2.waitKey(0)

# Chapter 4 Shapes and texts

# img=np.zeros((512,512,3),np.uint8)
# # print(img)
# cv2.line(img,(0,0),(300,300),(0,255,0),1)
# cv2.line(img,(512,0),(140,410),(0,255,0),1)
# cv2.rectangle(img,(0,0),(255,255),(10,20,250),1)
# cv2.circle(img,(255,255),100,(110,210,0),1)
# cv2.putText(img,"Allohu akbar!",(10,200),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),1)
# cv2.imshow("Surat",img)
# cv2.waitKey(0)