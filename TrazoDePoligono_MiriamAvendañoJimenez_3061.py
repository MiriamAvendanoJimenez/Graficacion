from abc import abstractproperty
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image
import math

plt.imshow(Image.open('fondo.png'))
coordenadas = []

def DDA(ejex, ejey, n):
    incx=[0 for i in range(n+1)]
    incy=[0 for i in range(n+1)]
    media=(n+1)/2
    for i in range (n, 0, -1):
        dx=abs(ejex[i-1]-ejex[i])
        dy=abs(ejey[i-1]-ejey[i])

        if(dx>dy):
            steps=dx
        else:
            steps=dy
        xinc=float(dx/steps)    
        yinc=float(dy/steps)
        
        if (ejex[i]>ejex[i-1]):
            xinc=round(-1*xinc, 1)
        else:
            xinc=round(xinc, 1)

        if (ejey[i]>ejey[i-1]):
            yinc=round(-1*yinc, 1)
        else: 
            yinc=round(yinc, 1)
    
        incx[i]=xinc
        incy[i]=yinc
    for i in range (0, n+1):
        x=ejex[i]
        y=ejey[i]
        
        for j in range (0, int(steps)):        
            plt.gca().add_patch(Rectangle((round(x), round(y)), 1, 1, linewidth=1, edgecolor='b', facecolor='none'))
            plt.ylim(0, 30)
            x=(x+incx[i])
            y=(y+incy[i])
            #print ("("+str(round(x))+", "+str(round(y))+")")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA')
    plt.show()


def bresenham(x1, y1, x2, y2):
    dx= (x2-x1)
    dy= (y2-y1)

    xinc= 1 if (dx>0) else -1
    yinc= 1 if (dy>0) else -1
    dx = abs(dx)
    dy = abs(dy)

    if (dx>dy):
        puntoxx, puntoxy, puntoyx, puntoyy = xinc, 0, 0, yinc
    else:
        dx, dy = dy, dx
        puntoxx, puntoxy, puntoyx, puntoyy = 0, yinc, xinc, 0

    p=2*dy-dx; y=0

    for x in range(dx + 1):
        yield x1 + x*puntoxx + y*puntoyx, y1 + x*puntoxy + y*puntoyy
        if (p>=0):
            y+=1
            p-=2*dx
        p+=2*dy

def coor(n, centro, long):  
    grados=0
    x1, y1 = centro
    x2, y2 = long 
    for i in range(n):
        coordenadas.append([])
        print(math.degrees(grados))
        for j in range(2): 
            if (j == 0):
                valor = round((x1+math.cos(grados)*(x2 - x1)-math.sin(grados) * (y2 - y1)))
                coordenadas[i].append(valor)
            else: 
                valor = round((y1 + math.sin(grados) * (x2 - y1) + math.cos(grados)  * (y2 - y1)))
                coordenadas[i].append(valor)
        grados+=math.radians(360/n)

def graficarFigura(n):
    resultado=[]
    for j in range(n):
        if (j==n-1):
            puntos = list(bresenham(coordenadas[j][0], 
            coordenadas[j][1], coordenadas[0][0], 
            coordenadas[0][1]))
            resultado+=puntos
        else:
            puntos = list(bresenham(coordenadas[j][0],
            coordenadas[j][1], 
            coordenadas[j+1][0], 
            coordenadas[j+1][1]))
            resultado+=puntos
            
    for i in resultado:
        plt.gca().add_patch(Rectangle(i, 1, 1, linewidth=1, edgecolor='b', facecolor='none'))
        plt.ylim(0, 30)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenham')


if __name__=='__main__':
    tipo= int(input("Ingresa el tipo de algoritmo:\n1. DDA\n2. Bresenham\n "))
    if (tipo==1):
        n= int(input("Ingresa el numero de lados: "))
        r= int(input("Ingrese la longitud de los lados, mayor al numero de lados: "))
        a= 360/n; inc= a
        angulos= [0 for i in range(n+1)]
        ejex= [0 for i in range(n+1)]
        ejey= [0 for i in range(n+1)]

        for i in range (0, n+1):
            angulos[i]= a
            a+=inc        
        
        for i in range (0, n+1):
            if (r>=10): r-=2
            x= r * math.cos(math.radians(angulos[i])) 
            x=round(x)
            ejex[i]= x
            y= r * math.sin(math.radians(angulos[i]))
            y= round(y)
            ejey[i]= y
            print(str(ejex[i])+", "+str(ejey[i]))
        DDA(ejex, ejey, n)

    elif(tipo==2):
        x2 = int(input("Ingrese la longitud de los lados: "))
        n= int(input("Ingrese el numero de lados: "))   
        x1 = 1; y1 = 1
        long= ((x1+(x2-1)), y1)
        centro = (x1, y1)
        coor(n, centro, long)
        graficarFigura(n)
        plt.show()
    else: print("OPCION NO VALIDA")