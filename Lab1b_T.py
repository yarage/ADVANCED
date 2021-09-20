#! /usr/bin/python3

from numpy import *

import matplotlib.pyplot as plt
from pylab import plot,show

import warnings
warnings.filterwarnings("ignore")

########################
# Gráfica de la resistencia de 20 ohmios:
########################

V = linspace(0,0.9,100)

# Recordemos: V = IR

I = (V/20)*1000


plot(V,I,color = 'orange',label = 'Curva IV (R = 20Ω)')
#plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
#plt.yticks([-10,0,10,20,30,40,50])
#Xtik = range(0,0.9,0.05)
#Ytik = range(-10,50,5)

Xtik = range(0,900,25)
Xtok = []
for n1 in Xtik:
    Xtok.append(n1/1000)

#Xtok = Xtok/100
Ytik = range(-10,50,1)
plt.xticks(Xtok)
plt.yticks(Ytik)
plt.xlim(0,0.9)
plt.ylim(-10,50)
plt.ylabel('Corriente(mA)')
plt.xlabel('Voltaje(V)')
plt.title('Curvas IV')
plt.legend()
plt.grid()
plt.show()


########################
# Gráficas con los datos y calculo de maximos
########################

###

#Funcion que recibe dos listas y las convierte en un array
#lo usamos con el fin de ordenar los datos y obtener un
#array para poderlo introducir en los metodos
def data_or(X1,Y1):
    #numero de datos
    n = len(X1)
    DAT = zeros([n,2],float64)
    for auxe in range(n):
        DAT[auxe,0] = X1[auxe]
        DAT[auxe,1] = Y1[auxe]
    return DAT

###

data1 = genfromtxt('L1B_Datos.txt',float64)

print("Los datos dados son:\n")
print("    I (mA) -  V (V)")
print(data1)

 
ct = len(data1)

y1 = data1[:,0]
x1 = data1[:,1]

#para ordenar de menor a mayor el voltaje
x,y = map(list, zip(*sorted(zip(x1, y1))))

plot(x,y,color = 'green',label = 'Curva IV - panelito')
plt.grid()
plt.legend()
plt.title('Curva IV - Panel')
plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (mA)')
plt.show()

Pot1 = []
for i in range(len(x)):
    Pot1.append(x[i]*y[i])


plot(x,y,'--',color = 'green',linewidth=0.5,label = 'Curva IV - panelito')
plot(x,y,'x',color = 'green')


plot(x,Pot1,'-.',color = 'blue',linewidth=0.5,label = 'Curva PV - panelito')
plot(x,Pot1,'x',color = 'blue')

plt.legend()
plt.title('Curvas IV - PV del panelito')
plt.xlabel('V (V)')
plt.grid()
plt.show()

error = std(Pot1)

maximo1 = max(Pot1)

vmax = x[Pot1.index(max(Pot1))]
print('El valor máximo de la potencia es: ', maximo1, 'mW al voltaje de:', vmax, 'V')
print('El error en este caso es calculado como la desviación estándar y es: ', error)




