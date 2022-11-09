# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np

T=np.array([[0,0,1],[1,1,1],[0,1,0]])
X=np.array([[1,0,1],[1,1,0],[0,0,1],[0,1,1]])
A=np.array([[1,1,1],[1,1,1],[1,1,1]])
W=np.array([[0.9,0.78,0.64],[-0.54,0.52,-0.11],[0.21,-0.09,0.23],[-0.03,-0.96,0.58]])
print("la matrice transpose de W")
print(np.transpose(W))

while(not (np.array_equal(A,T))):
    
    A= np.dot(np.transpose(W),X)
    print("la matrice transpose(W).X ")
    print(A) 
    
    for i in range(3):
        for j in range (3):
            if(A[i][j] >= 0):
                A[i][j] = 1
            else:
                A[i][j] = 0
    
    print(A)
    
    print(np.array_equal(A,T))
    if(not (np.array_equal(A,T))):
       
        tr = np.transpose(T-A)
        res = np.dot(X,tr)
        R = 0.3*res
        W=W+R
        
print(W)