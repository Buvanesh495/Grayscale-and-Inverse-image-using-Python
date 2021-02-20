#prerequsites :
#image path should be in the same folder where you save this python file
#You should have opencv libraries(If you don't have open command prompt and type     pip install opencv-python)

#import opencv
import cv2
#read the image as matrix (please change the filename that you want to use otherwise it will cause a traceback)
image = cv2.imread('Untitled.jpg')
#convert the rgb image to grayscale image
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#convert the grayscale image to neg image formula (S = L-1-r) where L=2^8=256 and r=matrix value of grayscale
neg_img = 255 - gray_img
#print all the matrix values of the images
print("Original image matrix - RGB")
print(image)
print("Grayscale image matrix")
print(gray_img)
print("Negative image matrix")
print(neg_img)
#create separate png files for grayscale and negative images
cv2.imshow('Original',image)
cv2.imwrite('untitled3.png',neg_img)
cv2.imshow("new image negative",neg_img)
cv2.imwrite('untitled2.png',gray_img)
cv2.imshow("new image grayscale",gray_img)
#Doesn't closes the img window until you closes it
cv2.waitKey()
cv2.destroyAllWindows()
