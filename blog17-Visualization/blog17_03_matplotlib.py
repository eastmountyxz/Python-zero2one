# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np  
import matplotlib.pyplot as plt

X = np.linspace(-np.pi,np.pi,256,endpoint=True)
C = np.cos(X)
S = np.sin(X)
plt.plot(X, C, color="blue", linewidth=2.0, linestyle="-", label="$sin(x)$")
plt.plot(X, S, color="red", linewidth=2.0, linestyle="--", label="$cos(x)$")
plt.legend()
plt.show() 
