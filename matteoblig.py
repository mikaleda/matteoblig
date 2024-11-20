import numpy as np
import matplotlib.pyplot as plt

v_s=5
R=100*10**3
C=100*10**(-6)

def v(t):
    return v_s*(1-np.exp(-t/(R*C)))

x_verdier=np.linspace(0,50,1000)
y_verdier=v(x_verdier)

sekunder=np.arange(0,51, 2)
spenning=[0, 0.94, 1.328, 2.19,  2.43, 2.87, 3.27, 3.51, 3.75, 3.92, 4.09, 4.17, 4.33, 4.41, 4.49, 4.54, 4.61, 4.66, 4.70, 4.72, 4.75, 4.78, 4.8, 4.81, 4.83, 4.84]


fig, ax = plt.subplots()
ax.plot(x_verdier, y_verdier)
ax.plot(sekunder, spenning)
ax.set_xlabel('Tid / s')
ax.set_ylabel('Spenning, v')
plt.show()
