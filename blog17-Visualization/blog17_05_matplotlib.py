# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt

#构造数据
x = np.random.randn(200)
y = np.random.randn(200)
print(x[:10])
print(y[:10])

#绘制散点图
plt.scatter(x, y)
plt.show()
