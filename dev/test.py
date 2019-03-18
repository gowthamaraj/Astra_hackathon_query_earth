import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread("compare/img1.jpg",0)
image2 = cv2.imread("compare/img2.jpg",0)
image1 = cv2.resize(image1,(650,550))
image2 = cv2.resize(image2,(650,550))


sift=cv2.xfeatures2d.SIFT_create()
kp1,des1=sift.detectAndCompute(image1,None)
kp2,des2=sift.detectAndCompute(image2,None) 

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params = dict(checks=50)

flann=cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

matchesMask = [[0,0] for i in range(len(matches))]


for i,(match1,match2) in enumerate(matches):
    if match1.distance<0.75*match2.distance:
        matchesMask[i]=[1,0]

draw_params= dict(matchColor=(0,0,255),singlePointColor=(255,0,0),matchesMask=matchesMask,flags=2)
flann_matches = cv2.drawMatchesKnn(image1,kp1,image2,kp2,matches,None,**draw_params)          

cv2.imshow("compare",flann_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('compare/compare.jpg',flann_matches)