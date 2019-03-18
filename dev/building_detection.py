import cv2
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread('house.jpg')
full = cv2.medianBlur(full,5)
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)

min = cv2.imread('hu.jpg')
min = cv2.cvtColor(min,cv2.COLOR_BGR2RGB)

x,y,z= min.shape
area=(x+4)*(y+5)

methods =['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for m in methods:
    full_copy = full.copy()
    method = eval(m)
    
    res= cv2.matchTemplate(full_copy,min,method)
    
    
    
my_method= eval('cv2.TM_CCOEFF')
res = cv2.matchTemplate(full,min,my_method)


tot=0
for i in range(422):
    for j in range(574):
        if res[i][j]>=240:
            tot=tot+1;
            
            
n = int(tot/area)
