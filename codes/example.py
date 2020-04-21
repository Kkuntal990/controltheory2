'''

Created by Kuntal Kokate
17.04.2020 at 1:14pm
Released under GNU GPL
'''
import numpy as np
import matplotlib.pyplot as plt
import control
import math
#values of omega (w)
OMEGA = np.linspace(-20, 20, 2001)

#defining transfer function
s = control.TransferFunction.s
G = 5/((s)*(s+1)*(s+3))

#Using library getting mag and phase of the transfer function for resp. omegas
MAG, PHASE, W = G.freqresp(OMEGA)


#unit circle
ag = np.linspace(0 ,2*np.pi, 1000)
mg = np.ones((1000,))

def find_nearest(array, value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1], idx-1
    else:
        return array[idx], idx
_, idx = find_nearest(MAG.reshape((2001,)), 1)

phi = -PHASE.reshape((2001,))[idx]
#plotting the polar plot
ax = plt.subplot(111, projection='polar')
#Slicing the array so that we can have smaller values of magnitude.
ax.plot(PHASE.reshape((2001,))[-960:], MAG.reshape((2001,))[-960:])
ax.plot(ag.reshape((1000,)), mg)   #plotting the unit circle
ax.plot(np.pi, 5/12, 'o', label = '$\omega_{pc}$')   #magnitude at phase cross over frequency.
ax.plot(phi, 1, 'o', label = '$\omega_{gc}$' )   #marking the point of gain cross over frequency.
ax.plot([np.pi, np.pi], [0, 5/12], 'g:')
#Showing the magnitude at phase cross over frequency
ax.annotate('|G(j$\omega_{pc}$)|', xy=(np.pi, 0.25), xytext=(3*np.pi/4, 0.75), arrowprops=dict(facecolor='black', shrink=0.001))
ax.plot([0, phi], [0, 1], '--')
ax.plot([-np.pi, (-np.pi+phi)/2, phi], [0.7, 0.7, 0.7], ":")
ax.text((-np.pi+ phi)/2, 1, '$\phi_{pm}$')
ax.plot(np.pi, 1, 'b+')
ax.text(np.pi-0.1, 1, '(-1,0)')
plt.legend(loc='upper_center')
plt.show()
