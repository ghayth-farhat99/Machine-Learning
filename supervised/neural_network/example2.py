import numpy as np


X=np.array([[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1]])
print("La matrice X:")
print(X)

print("La matrice T:")
T=np.array([[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1],[1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]])
print(T)

W=np.random.uniform(-0.99,0.99, size=(8,8)).round(2)#random values
print("La matrice initiale W:")
print(W)


A=np.array([[0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],[0,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]])
while(not (np.array_equal(A,T))):
    A= np.dot(np.transpose(W),X)
    for i in range(8):
        for j in range (18):
            if(A[i][j] >= 0):
                A[i][j] = 1
            else:
                A[i][j] = 0
    if(not (np.array_equal(A,T))):
        W=W+0.3*np.dot(X,np.transpose(T-A))

print("La matrice W finale:")
print(W)