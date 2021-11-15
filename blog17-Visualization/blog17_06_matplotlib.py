# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt

#构造数据
x = np.random.randn(200)
y = np.random.randn(200)
print(x[:10])
print(y[:10])
size = 50*np.random.randn(200) 
colors = np.random.rand(200) 

#绘制散点图
plt.scatter(x, y, s=size, c=colors)
plt.show()
