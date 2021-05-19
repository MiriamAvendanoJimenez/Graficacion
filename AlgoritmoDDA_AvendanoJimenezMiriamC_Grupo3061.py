import matplotlib.pyplot as plt
import numpy as np

def algorithmDDA(x1, y1, x2, y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if(dx>dy):
        steps=dx
    else:
        steps=dy
    
    xinc=float(dx/steps)
    yinc=float(dy/steps)

    xinc=round(xinc, 1)
    yinc=round(yinc, 1)

    for i in range (1, int (steps+1)) :
        plt.scatter(round(x1), round(y1))
        plt.plot(round(x1),round(y1), 'r.')
        x1=(x1+xinc)
        y1=(y1+yinc)
        print ("("+str(round(x1))+", "+str(round(y1))+")")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA')
    plt.show()

if __name__ == "__main__": 
    x1=int(input("Ingrese el valor de x1: "))    
    y1=int(input("Ingresa el valor de y1: "))    
    x2=int(input("Ingresa el valor de x2: "))    
    y2=int(input("Ingresa el valor de y2: "))

    algorithmDDA(x1, y1, x2, y2)
