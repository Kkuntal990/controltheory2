'''
Created by Kuntal Kokate
17.04.2020 at 1:14pm
Released under GNU GPL
'''
import numpy as np
import matplotlib.pyplot as plt
import control

#values of omega (w)
OMEGA = np.linspace(-20, 20, 2001)

#defining transfer function
s = control.TransferFunction.s
G = 1/((s**2)*(s+1)*(2*s+1))

#Using library getting mag and phase of the transfer function for resp. omegas
MAG, PHASE, W = G.freqresp(OMEGA)




#plotting the polar plot
ax = plt.subplot(111, projection='polar')

ax.plot(PHASE.reshape((2001,))[-995:-800],MAG.reshape((2001,))[-995:-800])
ax.plot(np.pi, 1, 'b+') #plotting (-1,0)
ax.text(-3*np.pi/4, 10, '(-1,0)')
plt.show()
