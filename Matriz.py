import numpy as np


def main():
    n=3
    m=4
    A = np.zeros((n,n))
    A=np.array([[1,2,3,5],[2,3,4,6],[3,4,5,6]])
    print_(A,n,m)
    print(" ---------")
    A=escalona(A,n)
    print_(A,n,m)

def print_(A,n,m):
    print('')
    for i in range(n):
        for j in range(m):
            if(A[i][j]>=0):
                print('',A[i][j],' ',end='')
            else:
                print(A[i][j],' ',end='')
        print('')

def troca_linha(A,i,j):
    v=A[i].copy()
    A[i]=A[j]
    A[j]=v
    print_(A,3)
    return A

def mult_linha(A,i,x,):
    A[i]=x*A[i]
    return A

def comb_linha(A,i,j,x):
    A[i]=A[i]+x*A[j]
    return A

def escalona(A,n):
    for i in range(n):
        passe = 0
        if A[i][i]==0:
            for j in range(i+1,n):
                if(A[j][i]!=0):
                    A=troca_linha(A,i,j)
                    break
                elif(j==n-1):
                    passe=1
        if (passe==0) :
            for k in range(i+1,n):
                A=comb_linha(A,k,i,-A[k][i]/A[i][i])
    return A


main()
