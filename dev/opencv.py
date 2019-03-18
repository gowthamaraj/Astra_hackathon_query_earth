import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread("./img1.jpg")
image2 = cv2.imread("./img2.jpg")
image1 = cv2.resize(image1,(650,550))
image2 = cv2.resize(image2,(650,550))



orb=cv2.ORB_create()
kp1,des1=orb.detectAndCompute(image1,None)
kp2,des2=orb.detectAndCompute(image2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches=bf.match(des1,des2)

matches = sorted(matches,key=lambda x:x.distance)

img_match= cv2.drawMatches(image1,kp1,image2,kp2,matches[:25],None,flags=2) 

cv2.imshow("compare",img_match)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('compare.jpg',img_match)

