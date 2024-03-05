import matplotlib.pyplot as plt
import numpy as np

func = input("Ange funktion")

def derivate(f,a,h):
    f = lambda x:eval(func)
    return((f(a+h)-f(a))/h)
    
print(derivate(func,2,0.00001))

def integrate(f,a,b,dx):
    
#plt.plot(x,y)
#plt.grid()
#plt.show()