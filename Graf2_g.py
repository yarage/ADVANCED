import numpy as np
import matplotlib.pyplot as plt
from pylab import plot,show
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

import warnings
warnings.filterwarnings("ignore")


img = plt.imread('2b_grec2.png')


# Create figure and add axes
fig = plt.figure(figsize=(12, 12))
#ax = fig.add_subplot(111)


# Create main axis
ax = fig.add_subplot(111)
#fig.subplots_adjust(bottom=0.2, top=0.75)
fig.subplots_adjust(bottom=0.2, top=0.7, left=0.0)

# Create axes for sliders
ax_a = fig.add_axes([0.3, 0.85, 0.4, 0.05])
ax_a.spines['top'].set_visible(True)
ax_a.spines['right'].set_visible(True)
ax_b = fig.add_axes([0.3, 0.92, 0.4, 0.05])
ax_b.spines['top'].set_visible(True)
ax_b.spines['right'].set_visible(True)

ax_c = fig.add_axes([0.3, 0.78, 0.4, 0.05])
ax_c.spines['top'].set_visible(True)
ax_c.spines['right'].set_visible(True)

# Create sliders
#s_a = Slider(ax=ax_a, label='Amplitud ', valmin=5000, valmax=50000, valfmt=' %1.1f Amp', facecolor='#cc7000')
s_a = Slider(ax=ax_a, label='Amplitud  ', valmin=1000, valmax=25000, valinit = 7050, valfmt=' %i', facecolor='#cc7000')

s_b = Slider(ax=ax_b, label='Frecuencia', valmin=1/np.pi, valmax=40,valinit=10.35, valfmt='%1.2f Hz', facecolor='#cc7000')


#s_c = Slider(ax=ax_c, label='Fase (D. horiz) ', valmin=0, valmax=10,valinit=1, valfmt='%1.0f ←/→', facecolor='#cc7000')
s_c = Slider(ax=ax_c, label='   (←/→)  ', valmin=0, valmax=10,valinit=2.5, valfmt='%1.2f', facecolor='#cc7000')


# Plot default data
x = np.linspace(0,100000,10000)

a_0 = 7050
b_0 = 10.35*2*np.pi/100000
c_0 = 2.5

def ondas(x,amp,f,ph):
    y = []
    for i in x:
        y.append(amp*np.sin(f*i + ph))
    return y
y = ondas(x,a_0,b_0,c_0)
f_d, = ax.plot(x, y, linewidth=2.5)


#img = plt.imread('2b_grec1.png')

#plt.imshow(img,extent=[120000,160000,-20000,20000])
#plt.show()


# Update values
def update(val):
    a = s_a.val
    b = s_b.val*2*np.pi/100000
    c = s_c.val
    f_d.set_data(x, ondas(x, a, b, c))
    fig.canvas.draw_idle()
s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)

#Slider.on_changed(update)
ax.imshow(img, extent = [0,100000,-35000,30000])
ax.set_xlim([0,100000])
ax.set_ylim([-35000,30000])
ax.set_xticks([0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000])
ax.set_xticklabels([0,'',0.1,'',0.2,'',0.3,'',0.4,'',0.5,'',0.6,'',0.7,'',0.8,'',0.9,'',1])
ax.set_xlabel('Time [s]')

ax.set_title('Gráfica 2. Modos de vibración')
###
#ax.grid()

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
modo1ax = plt.axes([0.65, 0.6, 0.165, 0.06])
button1 = Button(modo1ax, 'Primer modo', color='lightgoldenrodyellow', hovercolor='0.975')


def modo1(event):
    s_a.set_val(21000)
    s_b.set_val(4.79)
    s_c.set_val(3.45)
button1.on_clicked(modo1)


# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
modo2ax = plt.axes([0.65, 0.53, 0.165, 0.06])
button2 = Button(modo2ax, 'Segundo modo', color='lightgoldenrodyellow', hovercolor='0.975')


def modo2(event):
    s_a.set_val(5000)
    s_b.set_val(28.62)#28.80
    s_c.set_val(7.8)
button2.on_clicked(modo2)

###
#plt.title('Gráfica 1. Primer modo de vibración')
plt.show()


# Modulo de rigidez:
def modE(rho,A,L,I,frec,an):
    E = rho*A*L**4/I*(2*np.pi*frec/an**2)**2
    return E

d= 1.38e-2
E1 = modE(7850,np.pi*d**2/4,1.49,np.pi*d**4/64,4.79,1.875)
print("Mod E (1ra frec): ",E1)

E2 = modE(7850,np.pi*d**2/4,1.49,np.pi*d**4/64,28.62,4.694)
print("Mod E (2da frec): ",E2)

Ep = (E1+E2)/2

auxerror = [E1,E2]

error = np.std(auxerror)
print("El valor promedio de E es: ", Ep)
print("El error hallado con la desviación estándar es: ", error)


# Frecuencias teoricas:

E= 210e9
d = 0.0138
rho = 7850
A = np.pi*(d/2)**2
L = 1.49
I = np.pi*d**4/64

a1 = 1.875
f1 = (a1**2/(2*np.pi))*np.sqrt(E*I/(rho*A*L**4))

a2 = 4.694
f2 = (a2**2/(2*np.pi))*np.sqrt(E*I/(rho*A*L**4))

a3 = 7.855
f3 = (a3**2/(2*np.pi))*np.sqrt(E*I/(rho*A*L**4))

print("Las primeras tres frecuencias teoricas son: ",f1,f2,f3)




