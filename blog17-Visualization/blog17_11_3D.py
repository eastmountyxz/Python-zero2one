# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 绘制3D坐标的函数

fig = plt.figure()               #创建一个绘图对象
ax = Axes3D(fig)                 #用这个绘图对象创建一个Axes对象
X = np.arange(-2, 2, 0.25)       #X轴-2到2之间
Y = np.arange(-2, 2, 0.25)       #Y轴-2到2之间
print(Y)

X, Y = np.meshgrid(X, Y)         #用两个坐标轴上的点在平面上画格
R = np.sqrt(X**2 + Y**2)         #X和Y的平方和开根号
Z = np.sin(R)                    #计算sin函数赋值为Z坐标

#具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

#给三个坐标轴注明
ax.set_xlabel('x label', color='r')  
ax.set_ylabel('y label', color='g')  
ax.set_zlabel('z label', color='b')

plt.show()
