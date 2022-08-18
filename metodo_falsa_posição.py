import numpy as np
erro=0.000001
def achar_raiz_falsa(f,a,b):
    if(f(a)*f(b)>0):
        print("Erro, multiplicacão inicial positiva")
    else:
        while(1):
            c=(a*abs(f(a))+b*abs(f(b)))/(abs(f(a))+abs(f(b)))
            if(f(c)==0):
                return c
            elif(f(a)*f(c)<0):
                b=c
            else:
                a=c
            if(abs(f(a))<erro): #a-b tbm serve
                return a

def f(x):
    return np.cos(x)-x
res= achar_raiz_falsa(f,0,1)
print(res)