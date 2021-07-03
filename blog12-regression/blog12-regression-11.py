# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris    #导入数据集iris
  
#载入数据集  
iris = load_iris()  
print(iris.data)           #输出数据集  
print(iris.target)         #输出真实标签

#获取花卉两列数据集  
DD = iris.data  
X = [x[0] for x in DD]  
print(X)  
Y = [x[1] for x in DD]  
print(Y)  
  
#plt.scatter(X, Y, c=iris.target, marker='x')
plt.scatter(X[:50], Y[:50], color='red', marker='o', label='setosa') #前50个样本
plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor') #中间50个
plt.scatter(X[100:], Y[100:],color='green', marker='+', label='Virginica') #后50个样本
plt.legend(loc=2) #左上角
plt.show()
