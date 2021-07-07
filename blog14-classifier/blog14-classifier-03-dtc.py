# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-06
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

#导入数据集iris
'''
重点：分割数据集 构造训练集/测试集，80/20
     70%训练  0-40  50-90  100-140
     30%预测  40-50 90-100 140-150
'''
iris = load_iris()
train_data = np.concatenate((iris.data[0:40, :], iris.data[50:90, :], iris.data[100:140, :]), axis = 0)  #训练集
train_target = np.concatenate((iris.target[0:40], iris.target[50:90], iris.target[100:140]), axis = 0)  #训练集样本类别
test_data = np.concatenate((iris.data[40:50, :], iris.data[90:100, :], iris.data[140:150, :]), axis = 0)  #测试集
test_target = np.concatenate((iris.target[40:50], iris.target[90:100], iris.target[140:150]), axis = 0)  #测试集样本类别

#导入决策树DTC包
clf = DecisionTreeClassifier()
clf.fit(train_data, train_target)        #注意均使用训练数据集和样本类标
print(clf)
predict_target = clf.predict(test_data)  #测试集
print(predict_target)

#预测结果与真实结果比对
print(sum(predict_target == test_target))

#输出准确率 召回率 F值
print(metrics.classification_report(test_target, predict_target))
print(metrics.confusion_matrix(test_target, predict_target))

#获取花卉测试数据集两列数据
X = test_data
L1 = [n[0] for n in X]
L2 = [n[1] for n in X]

#绘图
plt.scatter(L1, L2, c=predict_target, marker='x')  #cmap=plt.cm.Paired
plt.title("DecisionTreeClassifier")
plt.show()
