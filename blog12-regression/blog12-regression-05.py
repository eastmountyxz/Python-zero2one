# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn import datasets
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#第一步 数据集划分
d = datasets.load_diabetes()  #数据 10*442
x = d.data
x_one = x[:,np.newaxis, 2]    #获取一个特征 第3列数据
y = d.target                  #获取的正确结果
x_train = x_one[:-42]         #训练集X [  0:400]
x_test = x_one[-42:]          #预测集X [401:442]
y_train = y[:-42]             #训练集Y [  0:400]
y_test = y[-42:]              #预测集Y [401:442]

#第二步 线性回归实现
clf = linear_model.LinearRegression()
print(clf)
clf.fit(x_train, y_train)
pre = clf.predict(x_test)
print('预测结果', pre)
print('真实结果', y_test)
   
#第三步 评价结果
cost = np.mean(y_test-pre)**2   #2次方
print('平方和计算:', cost)
print('系数', clf.coef_) 
print('截距', clf.intercept_)  
print('方差', clf.score(x_test, y_test))

#第四步 绘图
plt.plot(x_test, y_test, 'k.')      #散点图
plt.plot(x_test, pre, 'g-')        #预测回归直线
#绘制点到直线距离
for idx, m in enumerate(x_test):
    plt.plot([m, m],[y_test[idx], pre[idx]], 'r-')

plt.savefig('blog12-01.png', dpi=300) #保存图片
plt.show()      
