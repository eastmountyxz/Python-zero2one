# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt

#随机产生90个二维数组
x = np.random.rand(90,2)
print(x)

#numpy中ones()用来构造全一矩阵
label = list(np.ones(40))+list(2*np.ones(30))+list(3*np.ones(20)) #类标label为1、2、3
label = np.array(label)
print(label)
print(type(label))

idx1 = np.where(label == 1)
idx2 = np.where(label == 2)
idx3 = np.where(label == 3)

#绘图 参数：x值、y值、点样式、颜色、类标、粗细
p1 = plt.scatter(x[idx1,0], x[idx1,1], marker = 'x', color = 'r', label='1', s = 40)
p2 = plt.scatter(x[idx2,0], x[idx2,1], marker = '+', color = 'b', label='2', s = 30)
p3 = plt.scatter(x[idx3,0], x[idx3,1], marker = 'o', color = 'c', label='3', s = 20)
plt.legend(loc = 'upper right')
plt.show()
