import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import write

from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq



def LP(n):
    if n == 1:
        data_fileA = np.loadtxt(r'C:\Users\ERIC\Desktop\21-2\avanzada\proyecto\DATOS VENTANA\OFICIAL\w11.txt',dtype='str')
    if n == 2:
        data_fileA = np.loadtxt(r'C:\Users\ERIC\Desktop\21-2\avanzada\proyecto\DATOS VENTANA\OFICIAL\w12.txt',dtype='str')
    if n == 3:
        data_fileA = np.loadtxt(r'C:\Users\ERIC\Desktop\21-2\avanzada\proyecto\DATOS VENTANA\OFICIAL\w13.txt',dtype='str')
    if n == 4:
        data_fileA = np.loadtxt(r'C:\Users\ERIC\Desktop\21-2\avanzada\proyecto\DATOS VENTANA\OFICIAL\w14.txt',dtype='str')
    if n == 5:
        data_fileA = np.loadtxt(r'C:\Users\ERIC\Desktop\21-2\avanzada\proyecto\DATOS VENTANA\OFICIAL\w15.txt',dtype='str')

    zdata = data_fileA[:,2]
    znum = []
    for i in zdata:
        znum.append(float(i))


    zn = np.array(np.copy(znum))
    normalized_tone = np.int16((zn / max(zn)) * 32767)

    #yf = rfft(normalized_tone)
    yf = rfft(zn)
    xf = rfftfreq(len(zdata),1/204)


    fxf = np.abs(yf)
    fxf = list(fxf)

    dur = len(zdata)/204
    grt = np.linspace(0,dur,len(zdata))

    natexp = []

    if n == 1:

        # Gráfica de la señal:
        
        plt.plot(grt,zn)
        plt.title('Señal obtenida (Vibracion app)')
        plt.grid()
        plt.show()

        #Frecuencias experimentales:
        
        print('Primera frecuencia exp: ',xf[fxf.index(max(fxf[20:500]))])
        print('Segunda frecuencia exp: ',xf[fxf.index(max(fxf[500:1150]))])
        print('Tercera frecuencia exp: ',xf[fxf.index(max(fxf[1150:2500]))])
        print('Cuarta  frecuencia exp: ',xf[fxf.index(max(fxf[2500:4000]))])
        print('Quinta  frecuencia exp: ',xf[fxf.index(max(fxf[4000:4500]))])
        print('Sexta   frecuencia exp: ',xf[fxf.index(max(fxf[4500:7000]))])
        natexp.append(xf[fxf.index(max(fxf[20:500]))])
        natexp.append(xf[fxf.index(max(fxf[500:1150]))])
        natexp.append(xf[fxf.index(max(fxf[1150:2500]))])
        natexp.append(xf[fxf.index(max(fxf[2500:4000]))])
        natexp.append(xf[fxf.index(max(fxf[4000:4500]))])
        natexp.append(xf[fxf.index(max(fxf[4500:7000]))])

        # Grafica :

        plt.plot(xf, np.abs(yf))
        plt.title('Frecuencias encontradas usando FFT')

        # Para probar : 
        plt.plot(natexp,[20,20,20,20,20,20],'x')
        plt.xlabel('Frecuencia (Hz)')
        plt.grid()
        plt.show()

    if n == 2:
        
        # Gráfica de la señal:
        
        plt.plot(grt,zn)
        plt.title('Señal obtenida (Vibracion app)')
        plt.grid()
        plt.show()

        #Frecuencias experimentales:
        
        print('Primera frecuencia exp: ',xf[fxf.index(max(fxf[20:500]))])
        print('Segunda frecuencia exp: ',xf[fxf.index(max(fxf[500:1350]))])
        print('Tercera frecuencia exp: ',xf[fxf.index(max(fxf[1350:3000]))])
        print('Cuarta  frecuencia exp: ',xf[fxf.index(max(fxf[3000:4500]))])
        print('Quinta  frecuencia exp: ',xf[fxf.index(max(fxf[4500:5500]))])
        print('Sexta   frecuencia exp: ',xf[fxf.index(max(fxf[5500:7000]))])
        natexp.append(xf[fxf.index(max(fxf[20:500]))])
        natexp.append(xf[fxf.index(max(fxf[500:1350]))])
        natexp.append(xf[fxf.index(max(fxf[1350:3000]))])
        natexp.append(xf[fxf.index(max(fxf[3000:4500]))])
        natexp.append(xf[fxf.index(max(fxf[4500:5500]))])
        natexp.append(xf[fxf.index(max(fxf[5500:7000]))])

        # Grafica :

        plt.plot(xf, np.abs(yf))
        plt.title('Frecuencias encontradas usando FFT')

        # Para probar : 
        plt.plot(natexp,[20,20,20,20,20,20],'x')
        plt.xlabel('Frecuencia (Hz)')
        plt.grid()
        plt.show()
        
    if n == 3:

        # Gráfica de la señal:
        
        plt.plot(grt,zn)
        plt.title('Señal obtenida (Vibracion app)')
        plt.grid()
        plt.show()

        #Frecuencias experimentales:
        
        print('Primera frecuencia exp: ',xf[fxf.index(max(fxf[20:500]))])
        print('Segunda frecuencia exp: ',xf[fxf.index(max(fxf[500:1150]))])
        print('Tercera frecuencia exp: ',xf[fxf.index(max(fxf[1150:2500]))])
        print('Cuarta  frecuencia exp: ',xf[fxf.index(max(fxf[2500:4000]))])
        print('Quinta  frecuencia exp: ',xf[fxf.index(max(fxf[4000:5000]))])
        print('Sexta   frecuencia exp: ',xf[fxf.index(max(fxf[5000:7000]))])
        natexp.append(xf[fxf.index(max(fxf[20:500]))])
        natexp.append(xf[fxf.index(max(fxf[500:1150]))])
        natexp.append(xf[fxf.index(max(fxf[1150:2500]))])
        natexp.append(xf[fxf.index(max(fxf[2500:4000]))])
        natexp.append(xf[fxf.index(max(fxf[4000:5000]))])
        natexp.append(xf[fxf.index(max(fxf[5000:7000]))])

        # Grafica :

        plt.plot(xf, np.abs(yf))
        plt.title('Frecuencias encontradas usando FFT')

        # Para probar : 
        plt.plot(natexp,[20,20,20,20,20,20],'x')
        plt.xlabel('Frecuencia (Hz)')
        plt.grid()
        plt.show()
            
    if n == 4:

        # Gráfica de la señal:
        
        plt.plot(grt,zn)
        plt.title('Señal obtenida (Vibracion app)')
        plt.grid()
        plt.show()

        #Frecuencias experimentales:
        
        print('Primera frecuencia exp: ',xf[fxf.index(max(fxf[20:500]))])
        print('Segunda frecuencia exp: ',xf[fxf.index(max(fxf[500:1150]))])
        print('Tercera frecuencia exp: ',xf[fxf.index(max(fxf[1150:3000]))])
        print('Cuarta  frecuencia exp: ',xf[fxf.index(max(fxf[3000:4500]))])
        print('Quinta  frecuencia exp: ',xf[fxf.index(max(fxf[4500:5500]))])
        print('Sexta   frecuencia exp: ',xf[fxf.index(max(fxf[5500:7000]))])
        natexp.append(xf[fxf.index(max(fxf[20:500]))])
        natexp.append(xf[fxf.index(max(fxf[500:1150]))])
        natexp.append(xf[fxf.index(max(fxf[1150:3000]))])
        natexp.append(xf[fxf.index(max(fxf[3000:4500]))])
        natexp.append(xf[fxf.index(max(fxf[4500:5500]))])
        natexp.append(xf[fxf.index(max(fxf[5500:7000]))])

        # Grafica :

        plt.plot(xf, np.abs(yf))
        plt.title('Frecuencias encontradas usando FFT')

        # Para probar : 
        plt.plot(natexp,[20,20,20,20,20,20],'x')
        plt.xlabel('Frecuencia (Hz)')
        plt.grid()
        plt.show()

    if n == 5:

        # Gráfica de la señal:
        
        plt.plot(grt,zn)
        plt.title('Señal obtenida (Vibracion app)')
        plt.grid()
        plt.show()

        #Frecuencias experimentales:
        
        print('Primera frecuencia exp: ',xf[fxf.index(max(fxf[20:500]))])
        print('Segunda frecuencia exp: ',xf[fxf.index(max(fxf[500:1500]))])
        print('Tercera frecuencia exp: ',xf[fxf.index(max(fxf[1500:4000]))])
        print('Cuarta  frecuencia exp: ',xf[fxf.index(max(fxf[4000:5000]))])
        print('Quinta  frecuencia exp: ',xf[fxf.index(max(fxf[5000:7000]))])
        print('Sexta   frecuencia exp: ',xf[fxf.index(max(fxf[7000:7500]))])
        natexp.append(xf[fxf.index(max(fxf[20:500]))])
        natexp.append(xf[fxf.index(max(fxf[500:1500]))])
        natexp.append(xf[fxf.index(max(fxf[1500:4000]))])
        natexp.append(xf[fxf.index(max(fxf[4000:5000]))])
        natexp.append(xf[fxf.index(max(fxf[5000:7000]))])
        natexp.append(xf[fxf.index(max(fxf[7000:7500]))])

        # Grafica :

        plt.plot(xf, np.abs(yf))
        plt.title('Frecuencias encontradas usando FFT')

        # Para probar : 
        plt.plot(natexp,[20,20,20,20,20,20],'x')
        plt.xlabel('Frecuencia (Hz)')
        plt.grid()
        plt.show()


    return natexp


print('\nPrimer conjunto de datos: \n')
FNE1 = LP(1)
FNE1 = np.array(FNE1)

print('\nSegundo conjunto de datos: \n')
FNE2 = LP(2)
FNE2 = np.array(FNE2)

print('\nTercero conjunto de datos: \n')
FNE3 = LP(3)
FNE3 = np.array(FNE3)

print('\nCuarto conjunto de datos: \n')
FNE4 = LP(4)
FNE4 = np.array(FNE4)

print('\nQuinto conjunto de datos: \n')
FNE5 = LP(5)
FNE5 = np.array(FNE5)


prom = (FNE1 + FNE2 + FNE3 + FNE4 + FNE5)/5

errores = []
for k in range(6):
    aux = []
    aux.append(FNE1[k])
    aux.append(FNE2[k])
    aux.append(FNE3[k])
    aux.append(FNE4[k])
    aux.append(FNE5[k])
    errores.append(np.std(aux))

print('\nFrecuencias de vibración en promedio: \n')
for i in range(6):
    print(' Modo de vibracion ', i+1, ' :', prom[i], ' ± ', errores[i])





