import cv2
import numpy as np
import matplotlib.pyplot as plt

min= cv2.imread('grass.jpg')
#min = cv2.medianBlur(min,5)
min = cv2.cvtColor(min,cv2.COLOR_BGR2RGB)
#min = cv2.resize(min,(10,10))
tre1 = cv2.imread('tre1.jpg')
tre1 = cv2.cvtColor(tre1,cv2.COLOR_BGR2RGB)
tre2 = cv2.imread('tre2.jpg')
tre2 = cv2.cvtColor(tre2,cv2.COLOR_BGR2RGB)
tre3 = cv2.imread('tre3.jpg')
tre3 = cv2.cvtColor(tre3,cv2.COLOR_BGR2RGB)


x,y,z= min.shape
area=(x)*(y)




    
my_method= eval('cv2.TM_CCORR_NORMED')
res1 = cv2.matchTemplate(tre1,min,my_method)
res2 = cv2.matchTemplate(tre2,min,my_method)
res3 = cv2.matchTemplate(tre3,min,my_method)



x3,y3=res3.shape
area3=x3*y3

x2,y2=res2.shape
area2=x2*y2

x1,y1=res1.shape
area1=x1*y1


tot1=0
tot2=0
tot3=0

for i in range(x3):
    for j in range(y3):
        if res3[i][j]>0.9600:
            tot3=tot3+1;
            
            
for i in range(x2):
    for j in range(y2):
        if res2[i][j]>0.9600:
            tot2=tot2+1;
            
            
for i in range(x1):
    for j in range(y1):
        if res1[i][j]>0.9600:
            tot1=tot1+1;            
            
            
            
            
            
            
            
            
            
            