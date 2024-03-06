import matplotlib.pyplot as plt
import numpy as np

func = input("Ange funktion")

#def derivate(f,a,h):
#    f = lambda x:eval(func)
#    return((f(a+h)-f(a))/h)
    
#print(derivate(func,2,0.00001))

def integrate(f,a,b,dx):
    int = 0
    f = lambda x:eval(func)
    while a < b:
        int = int + (f(a)*dx)
        a = a + dx
    return int
print(integrate(func,0,2,0.0001))

    
#plt.plot(x,y)
#plt.grid()
#plt.show()