#! /usr/bin/python3

from numpy import *

import matplotlib.pyplot as plt
from pylab import plot,show

import warnings
warnings.filterwarnings("ignore")



N = [0,1,2,3,4,5]
d_N = []

def espesor(N,long_onda,nf):
    return (N+1/2)*long_onda/(2*nf)


for i in N:
    d_N.append(espesor(i,475e-09,1.33))

for c in N:
    print('# máx. de reflexión: ',c+1,' Espesor: ', d_N[c])



plt.plot([1,2,3,4,5,6],d_N,'--',color = 'orange')
plt.plot([1,2,3,4,5,6],d_N,'x',color = 'black')
plt.grid()
plt.ylabel('Espesor (μm)')
plt.xlabel('Nro. de máximo de reflexión')
plt.show()
