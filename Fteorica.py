#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#from pylab import plot,show

import warnings
warnings.filterwarnings("ignore")



def naturalfreq(eigenv,E,h,a,gamma,poisson):
    #return (eigenv/(2*np.pi*a**2))*((E*h**2)/(12*gamma*(1-poisson**2)))**(1/2)
    #return (eigenv/(2*np.pi*a**2))*((E*h**3)/(12*gamma*(1-poisson**2)))**(1/2)
    return (eigenv/(2*np.pi*a**2))*((E*h**3)/(12*gamma*(1-poisson**2)))**(1/2)


a = 1.30
b = 0.657

# Modulo E: 48 - 83 e09
E = 50e9

# Gamma 14.4 - 16.8
gamma = 14.4
#gamma = 15.6
#gamma = 16.8

poisson = 0.333
h = 0.006

# m:
eigenvalues1 = [10.37,15.68,25.70,40.51,60.21,84.84]
eigenvalues2 = [39.72,45.00,55.25,70.34,90.23,115.0]
eigenvalues3 = [88.81,94.08,104.3,119.5,139.6,164.5]
eigenvalues4 = [157.6,162.9,173.1,188.3,208.4,233.4]


#dens = 16.8
dens = 16.8



print('\nM = 1\n')
for i in range(6):
    print(' Modo : ( 1',i+1,') frec: ',naturalfreq(eigenvalues1[i],E,h,a,dens,poisson))

print('\nM = 2\n')
for i in range(6):
    print(' Modo : ( 2',i+1,') frec: ',naturalfreq(eigenvalues2[i],E,h,a,dens,poisson))

print('\nM = 3\n')
for i in range(6):
    print(' Modo : ( 3',i+1,') frec: ',naturalfreq(eigenvalues3[i],E,h,a,dens,poisson))

print('\nM = 4\n')
for i in range(6):
    print(' Modo : ( 4',i+1,') frec: ',naturalfreq(eigenvalues4[i],E,h,a,dens,poisson))
    
