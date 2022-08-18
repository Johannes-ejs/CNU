import numpy as np
from scipy.misc import derivative
erro=0.001
limite=1000
def f(x):
    return np.cos(x)-x
def df(x):
    return derivative(f,x)
def i(x):
    return x-f(x)/df(x)
def achar_raiz_fixa(i,x0):
    cont = 0
    while(abs(i(x0)-x0)>erro):
        x0=i(x0)
        print(x0)
        cont+=1
        if(cont==limite):
            print("excedeu número de tentativas")
            exit()
    return x0

res= achar_raiz_fixa(i,0.5)
print(res)
