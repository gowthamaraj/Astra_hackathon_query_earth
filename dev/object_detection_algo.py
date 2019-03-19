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




import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread("./img1.jpg")
image2 = cv2.imread("./img2.jpg")
image1 = cv2.resize(image1,(650,550))
image2 = cv2.resize(image2,(650,550))


sift=cv2.xfeatures2d.SIFT_create()
kp1,des1=sift.detectAndCompute(image1,None)
kp2,des2=sift.detectAndCompute(image2,None)
bf=cv2.BFMatcher()

matches= bf.knnMatch(des1,des2,k=2)

good=[]

for match1,match2 in matches:
    if match1.distance<0.7*match2.distance:
        good.append([match1])
        

sift_matches = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good,None,flags=2)    
cv2.imshow("compare",sift_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('compare.jpg',sift_matches)




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





