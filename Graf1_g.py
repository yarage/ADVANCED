#! /usr/bin/python3

#from numpy import *

import numpy as np

import matplotlib.pyplot as plt
from pylab import plot,show


#from matplotlib.pyplot import figure


import warnings
warnings.filterwarnings("ignore")

from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

from matplotlib.widgets import Button


img = plt.imread('2b_grec1.png')


# Create figure and add axes
fig = plt.figure(figsize=(12, 12))
# Create main axis
ax = fig.add_subplot(111)
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
s_a = Slider(ax=ax_a, label='Amplitud  ', valmin=5000, valmax=25000, valinit = 15000, valfmt=' %i', facecolor='#cc7000')
s_b = Slider(ax=ax_b, label='Frecuencia', valmin=1/np.pi, valmax=7,valinit=4.88, valfmt='%1.2f Hz', facecolor='#cc7000')
s_c = Slider(ax=ax_c, label='   (←/→)  ', valmin=0, valmax=10,valinit=4.5, valfmt='%1.2f', facecolor='#cc7000')


# Plot default data
x = np.linspace(120000,160000,10000)

a_0 = 15000
b_0 = 4.88*2*np.pi/20000
c_0 = 4.5

def ondas(x,amp,f,ph):
    y = []
    for i in x:
        y.append(amp*np.sin(f*i + ph))
    return y
y = ondas(x,a_0,b_0,c_0)
f_d, = ax.plot(x, y, linewidth=2.5)


# Update values
def update(val):
    a = s_a.val
    b = s_b.val*2*np.pi/20000
    c = s_c.val
    f_d.set_data(x, ondas(x, a, b, c))
    fig.canvas.draw_idle()
s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)

#Slider.on_changed(update)
ax.imshow(img, extent = [120000,160000,-20000,20000])
ax.set_xlim([120000,160000])
ax.set_ylim([-20000,20000])
ax.set_xticklabels([6.0,'',6.5,'',7.0,'',7.5,'',8.0])
ax.set_xlabel('Time [s]')

ax.set_title('Gráfica 1. Primer modo de vibración')

#ax.grid()
# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.65, 0.6, 0.165, 0.06])
button = Button(resetax, 'RESET\n(Primer modo de vibración)', color='lightgoldenrodyellow', hovercolor='0.975')


def reset(event):
    s_a.reset()
    s_b.reset()
    s_c.reset()
button.on_clicked(reset)

plt.show()

