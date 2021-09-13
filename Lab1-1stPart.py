#! /usr/bin/python3

from numpy import *

import matplotlib.pyplot as plt
from pylab import plot,show

import warnings
warnings.filterwarnings("ignore")


y11 = linspace(23,44,100)
y12 = linspace(-10,23,50)

y1 = concatenate((y12, y11), axis=None)

y1 = y1[::-1]

x11 = linspace(0,24.5,100)
x12 = linspace(24.5,25,50)

x1 = concatenate((x11, x12), axis=None)

pot1 = [x*y for x,y in zip(x1,y1)]


plot(x1,y1)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
plt.yticks([-10,0,10,20,30,40,50])
plt.grid()
plt.show()


plot(x1,y1)
plot(x1,pot1)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
#plt.yticks([-10,0,10,20,30,40,50])
plt.grid()
plt.show()

############
############

y21 = linspace(0,24,100)
y22 = linspace(-10,0,50)

y2 = concatenate((y22, y21), axis=None)

y2 = y2[::-1]

x21 = linspace(0,24.75,100)
x22 = linspace(24.75,25,50)

x2 = concatenate((x21, x22), axis=None)

pot2 = [x*y for x,y in zip(x2,y2)]

plot(x2,y2)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
plt.yticks([-10,0,10,20,30,40,50])
plt.grid()
plt.show()


plot(x2,y2)
plot(x2,pot2)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
#plt.yticks([-10,0,10,20,30,40,50])
plt.grid()
plt.show()



plot(x1,y1,color = 'blue',label = '35 C. buenas + 1 media m.')
plot(x1,pot1, '--',color ='blue', label ='Potencia')
plot(x2,y2,color = 'green',label = '35 C. buenas + 1 mala')
plot(x2,pot2, '--',color = 'green', label ='Potencia')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
#plt.yticks([-10,0,10,20,30,40,50])
plt.xlabel('Voltaje(V)')
plt.title('Curvas IV - PV')
plt.legend()
plt.grid()
plt.show()



print('Máxima potencia curva azul: ', max(pot1))
print('Voltaje del máximo: ', x2[pot1.index(max(pot1))])

print('Máxima potencia curva verde: ', max(pot2))
print('Voltaje del máximo: ', x2[pot2.index(max(pot2))])




plot(x1,y1,color = 'blue',label = '35 C. buenas + 1 media m.')
plot(x2,y2,color = 'green',label = '35 C. buenas + 1 mala')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26])
plt.yticks([-10,0,10,20,30,40,50])
plt.ylabel('Corriente(mA)')
plt.xlabel('Voltaje(V)')
plt.title('Curvas IV')
plt.legend()
plt.grid()
plt.show()


