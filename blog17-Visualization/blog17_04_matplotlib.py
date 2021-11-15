# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8 , 8, 1024)
y1 = 0.618*np.abs(x) - 0.8* np.sqrt(64-x**2)
y2 = 0.618*np.abs(x) + 0.8* np.sqrt(64-x**2) 
plt.plot(x, y1, color = 'r')
plt.plot(x, y2, color = 'r')
plt.show()
