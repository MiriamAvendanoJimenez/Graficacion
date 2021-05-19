import matplotlib.pyplot as plt
import numpy as np

def algorithmBresenham(x1, y1, x2, y2):
    x=x1
    y=y1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    p=2*dy-dx

    for i in range(x1, x2):
        plt.scatter(round(x), round(y))
        plt.plot(round(x), round(y), color='red')
        x+=1
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y+=1

        print ("("+str(round(x))+", "+str(round(y))+")")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA')
    plt.show()

if __name__ == "__main__": 
    x1=int(input("Ingrese el valor de x1: "))    
    y1=int(input("Ingresa el valor de y1: "))    
    x2=int(input("Ingresa el valor de x2: "))    
    y2=int(input("Ingresa el valor de y2: "))

    algorithmBresenham(x1, y1, x2, y2)
