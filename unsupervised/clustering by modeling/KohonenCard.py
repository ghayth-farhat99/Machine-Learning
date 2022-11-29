from math import *
e1=[1,1,1,1,0,0]
e2=[0,1,1,0,0,1]
e3=[1,0,0,0,1,0]
e4=[1,0,1,1,0,0]
e=[[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,0,0,1],[0,0,1,0],[0,1,0,0]]
voisins = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
w=[[-0.6,0.4,-0.2,0.6],[0.3,-0.2,-0.3,0.7],[0.8,0.4,0.9,-0.5],[-0.3,-0.2,0.7,-0.7],[0.2,-0.4,0.5,0.3],[0.3,-0.8,0.4,0.8]]

for p in range(4):
    d=[]
    for j in range(4):
        sum = 0
        for i in range(6):
            sum +=((e[i][p]-w[i][j])**2)
        d.append(sqrt(sum))
    print('**********************************************************************************************************')
    print('la liste de distance : ',d)
    indice = d.index(min(d))
    print('le point : ', p ) 
    print('la noeude de le point : ',indice)
    for i in range(6):
        w[i][indice]=w[i][indice]+0.75 * (e[i][p]-w[i][indice])
        for j in range(4):
            if(voisins[indice][j] == 1):
                for k in range(6):
                    w[k][j]=w[k][j]+0.3 * (e[k][p]-w[k][j])
    print('la matrice w : ', w )