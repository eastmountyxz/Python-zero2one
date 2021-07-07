# -*- coding: utf-8 -*-  
import os 
import numpy as np
path = "wine/wine.txt"
data = np.loadtxt(path,dtype=float,delimiter=",")
print(data)

yy, x = np.split(data, (1,), axis=1)
print(yy.shape, x.shape)
y = []
for n in yy:
    y.append(int(n))

train_data = np.concatenate((x[0:40,:], x[60:100,:], x[140:160,:]), axis = 0)  #训练集
train_target = np.concatenate((y[0:40], y[60:100], y[140:160]), axis = 0)      #样本类别
test_data = np.concatenate((x[40:60, :], x[100:140, :], x[160:,:]), axis = 0)  #测试集
test_target = np.concatenate((y[40:60], y[100:140], y[160:]), axis = 0)        #样本类别

print(train_data.shape, train_target.shape)
print(test_data.shape, test_target.shape)
