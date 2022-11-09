import numpy as np
import random
from math import *

# X0=[0,4]
# X1=[0,6]
# X2=[1,5]
# X3=[2,4]
# X4=[3,2]
# X5=[3,4]
# X6=[3,5]
# X7=[4,1]k
# X8=[4,2]
# X9=[4,3]
# X10=[5,0]

X=np.array([[0,4],[0,6],[1,5],[2,4],[3,2],[3,4],[3,5],[4,1],[4,2],[4,3],[5,0]])
c1=[]
c2=[]
c3=[]
Xg1 = 0
Yg1 = 0
Xg2 = 0
Yg2 = 0
Xg3 = 0
Yg3 = 0
Xgg1 = 0
Ygg1 = 0
Xgg2 = 0
Ygg2 = 0
Xgg3 = 0
Ygg3 = 0
L=[0,1,2,3,4,5,6,7,8,9,10]
while(L != []):
    index = random.randint(1,3)
    element=random.choice(L)
    n=L.index(element)
    L.pop(n)
    if(index == 1):
        c1.append(element)
    else :
        if(index == 2):
            c2.append(element)
        else : 
            c3.append(element)

print("c1 :",c1)
print("c2 :",c2)
print("c3 :",c3)

for i in c1:
    Xg1 =Xg1 + X[i][0]
    Yg1 =Yg1 + X[i][1]
if(c1 != []):
    Xg1 = Xg1/len(c1)
    Yg1 = Yg1/len(c1)

for i in c2:
    Xg2 =Xg2 + X[i][0]
    Yg2 =Yg2 + X[i][1]
if(c2 != []):
    Xg2 = Xg2/len(c2)
    Yg2 = Yg2/len(c2)

for i in c3:
    Xg3 =Xg3 + X[i][0]
    Yg3 =Yg3 + X[i][1]
if(c3 != []):
    Xg3 = Xg3/len(c3)
    Yg3 = Yg3/len(c3)

print("c1 :",Xg1,Yg1)
print("c2 :",Xg2,Yg2)
print("c3 :",Xg3,Yg3)

while((Xgg1 != Xg1)or(Ygg1 != Yg1)or(Xgg2 != Xg2)or(Ygg2 != Yg2)or(Xgg3 != Xg3)or(Ygg3 != Yg3)):
    c1=[]
    c2=[]
    c3=[]
    Xgg1 = Xg1
    Ygg1 = Yg1
    Xgg2 = Xg2
    Ygg2 = Yg2
    Xgg3 = Xg3
    Ygg3 = Yg3
    for i in range (11):
        d1=sqrt((X[i][1]-Yg1)**2+(X[i][0]-Xg1)**2)
        d2=sqrt((X[i][1]-Yg2)**2+(X[i][0]-Xg2)**2)
        d3=sqrt((X[i][1]-Yg3)**2+(X[i][0]-Xg3)**2)
        Dmin = min(d1,d2,d3)
        if(Dmin == d1):
            c1.append(i)
        else:
            if(Dmin == d2):
                c2.append(i)
            else:
                c3.append(i)
    print("c1 :",c1)
    print("c2 :",c2)
    print("c3 :",c3)
    
    for i in c1:
        Xg1 =Xg1 + X[i][0]
        Yg1 =Yg1 + X[i][1]
    if(c1 != []):
        Xg1 = Xg1/len(c1)
        Yg1 = Yg1/len(c1)

    for i in c2:
        Xg2 =Xg2 + X[i][0]
        Yg2 =Yg2 + X[i][1]
    if(c2 != []):
        Xg2 = Xg2/len(c2)
        Yg2 = Yg2/len(c2)

    for i in c3:
        Xg3 =Xg3 + X[i][0]
        Yg3 =Yg3 + X[i][1]
    if(c3 != []):
        Xg3 = Xg3/len(c3)
        Yg3 = Yg3/len(c3)

print("c1 :",Xg1,Yg1)
print("c2 :",Xg2,Yg2)
print("c3 :",Xg3,Yg3)