import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image

plt.imshow(Image.open('fondo.png'))

def DDATR(x1, y1, x2, y2, y3):
    x1r=x1; y1r=y1; x2-=1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x3=x2
    if(dx>dy):
        steps=dx
    else:
        steps=dy
    xinc=float(dx/steps)    
    yinc=float(dy/steps)    
    xinc=round(xinc, 1)
    yinc=round(yinc, 1)

    dx1= abs(x3-x1)
    dy1= abs(y3-y1)
    if(dx1>dy1):
        steps1=dx1
    else:
        steps1=dy1
    xinc1=float(dx1/steps1)
    yinc1=float(dy1/steps1)
    xinc1=round(xinc1, 1)
    yinc1=round(yinc1, 1)

    dx2= abs(x3-x2)
    dy2= abs(y3-y2)
    if(dx2>dy2):
        steps2=dx2
    else:
        steps2=dy2
    xinc2=float(dx2/steps2)
    yinc2=float(dy2/steps2)
    xinc2=round(xinc2, 1)
    yinc2=round(yinc2, 1)

    for i in range (0, int (steps1)):
        plt.gca().add_patch(Rectangle((round(x1), round(y1)), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        x1=(x1+xinc1); y1=(y1+yinc1)
        print ("("+str(round(x1))+", "+str(round(y1))+")")

    for i in range (0, int (steps)):
        plt.gca().add_patch(Rectangle((x1r, y1r), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))        
        plt.ylim(0, 30)
        x1r=(x1r+xinc); y1r=(y1r+yinc)                
        print ("("+str(round(x1r))+", "+str(round(y1r))+")") 

    for i in range (0, int (steps2)):
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))        
        plt.ylim(0, 30)
        x2=(x2+xinc2); y2=(y2+yinc2)                
        print ("("+str(round(x2))+", "+str(round(y2))+")") 

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA')
    plt.show()

def BresenhamTR(x1, y1, x2, y2, y3):
    x=x1; y=y1; x2-=1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    p=2*dy-dx
    x3=x2; 

    dx1=abs(x3-x1)
    dy1=abs(y3-y1)
    p1=2*dy1-dx1

    dx2=abs(x3-x2)
    dy2=abs(y3-y2)
    p2=2*dy2-dx2
    
    while (x<x3):
        plt.gca().add_patch(Rectangle((round(x), round(y)), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        x+=1
        if (p1<0):
            p1=p1+2*dy1
        else:
            p1=p1+(2*dy1)-(2*dx1)
            y+=1

        print ("("+str(round(x))+", "+str(round(y))+")")

    while (x1<=x2):
        plt.gca().add_patch(Rectangle((x1, y1), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        x1+=1
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y1+=1

        print ("("+str(round(x1))+", "+str(round(y1))+")")
    
    while (y2<y3):
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='r', facecolor='none'))
        plt.ylim(0, 30)
        y2+=1
        if (p2<0):
            p2=p2+2*dy2
            x2+=1
        else:
            p2=p2+(2*dy2)-(2*dx2)

        print ("("+str(round(x2))+", "+str(round(y2))+")")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenhams')
    plt.show()

if __name__=='__main__':
    tipo=int(input("Ingrese el valor del algoritmo a usar:\n1. Algoritmo DDA\n2. Algoritmo Bresenham\n"))
    x1=int(input("Ingrese el valor de x1: "))    
    y1=int(input("Ingresa el valor de y1: "))   
    x2=int(input("Ingresa la base del triangulo rectangulo: "))
    y3=int(input("Ingrese la altura del triangulo rectangulo: "))
    y2=y1
    if (x2<0): x2=x2*-1
    if (y3<0): y3=y3*-1

    if (tipo==1):
        DDATR(x1, y1, (x2+x1), y2, (y3+y1))
    elif (tipo==2):
        BresenhamTR(x1, y1, (x2+x1), y2, (y3+y1))
    else: print("OPCION NO VALIDA")