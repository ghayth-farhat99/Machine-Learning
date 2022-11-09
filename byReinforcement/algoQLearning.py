
import numpy as np

import random


action=[]
list=['H','B','G','D']
matrice=np.array([[1,0,2],[3,4,5],[6,0,7]])
i=0
j =0
E = matrice[i][j]
S=E
F = matrice[2][2]
R=np.array([[0,2,0,0],[0,2,0,0],[-2,-2,0,2],[0,0,-3,3],[-3,4,-3,0],[2,0,0,0],[0,0,0,0]])
Q = np.zeros((7,4))
T=np.array([[0,1,0,0],[0,1,0,0],[1,1,0,1],[0,0,1,1],[1,1,1,0],[1,0,0,0],[0,0,0,0]])
print("la position initiale : ",E)
print("la liste des actions possibles: ",list)
print("la position finale : ",F)
print("la matrice Q initiale : ",Q)
print("la matrice R initiale : ",R)
print("la matrice T initiale : ",T)
for k in range(4):
    if(T[S-1][k]==1):
        action.append(list[k])

print(action)
if(action[0] =='B'):
    i+=1
    S1=matrice[i][j]
    Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
    S = S1
print("la matrice Q apres la premiere iteration : ",Q)
print("la position  apres la premiere iteration : ",S)

#tantque la position s != de la position finale F 

while(S != F):
    action2 = []
    action3 = []
    for k in range(4):
        if(T[S-1][k]==1):
            action2.append(list[k])
# action2 la liste des actions possibles, exemple pour la position 3 ona 3 actions possibles {'H','B','D'}
    
    x = random.random()
    print("x:",x)
    # x un reel aleatoire entre [0,1] si x<0.5 on faire une exploration sinon une exploitation
    if(x<0.5):
        random_index = random.randint(0,len(action2)-1)
        #choisir un ele random de la liste action3 qui a les actions possibles pour l'exploitation
        y = action2[random_index]
        if(y=='H'):
            i-=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(y=='B'):
            i+=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(y=='G'):
            j-=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(y=='D'):
            j+=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
    else:
        for z in range (4):
            if(Q[S-1][z] == max(Q[S-1])):
                if(list[z] in action2):
                    action3.append(list[z])
        #choisir un ele random de la liste action3 qui a les actions possibles pour l'exploitation
        random_ind = random.randint(0,len(action3)-1)
        ind = action3[random_ind]
        if(ind== 'H'):
            i-=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(ind== 'B'):
            i+=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(ind== 'G'):
            j-=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
        if(ind== 'D'):
            j+=1
            S1=matrice[i][j]
            Q[S-1][1]=0.7*Q[S-1][1]+0.3*(R[S-1][1]+0.5*max(Q[S1-1]))
            S = S1
    print(S)
print("la matrice finale Q",Q)