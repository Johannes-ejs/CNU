import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(x)-x
def plotar(f,a,b):
    x=np.linspace(a,b)
    plt.plot(x,f(x))
    plt.plot([a,b],[0,0])
    plt.grid()
    plt.show()

plotar(f,0,1)