# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-06

#导入数据集iris
from sklearn.datasets import load_iris 
iris = load_iris()
print(iris.data)           #输出数据集
print(iris.target)         #输出真实标签
print(len(iris.target))
print(iris.data.shape)     #150个样本 每个样本4个特征

#导入决策树DTC包
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(iris.data, iris.target)        #训练
print(clf)
predicted = clf.predict(iris.data)     #预测

#获取花卉两列数据集
X = iris.data
L1 = [x[0] for x in X]
L2 = [x[1] for x in X]

#绘图
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predicted, marker='x')  #cmap=plt.cm.Paired
plt.title("DTC")
plt.show()
