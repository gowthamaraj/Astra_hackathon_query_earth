
    
    
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread("dynamic/images/img1.jpg",0)
image2 = cv2.imread("dynamic/images/img2.jpg",0)
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

cv2.destroyAllWindows()
cv2.imwrite('dynamic/images/compare.jpg',flann_matches)


from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def hello_there():
    return render_template("index.html")

@app.route('/index')
def comp():
    return render_template("index.html")

@app.route('/search')
def sear():
    return render_template("search.html")

@app.route('/trend')
def tren():
    return render_template("trend.html")
if __name__ == "__main__":
    app.run(debug=True, port=8080)
    