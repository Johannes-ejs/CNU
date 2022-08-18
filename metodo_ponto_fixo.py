import numpy as np
erro=0.001
limite=1000
def f(x):
    return np.cos(x)-x
def i(x):
    return f(x)-x
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
