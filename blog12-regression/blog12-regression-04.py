# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn import datasets  
import matplotlib.pyplot as plt  
from sklearn import linear_model
import numpy as np  

#数据集划分
diabetes = datasets.load_diabetes()                #载入数据  
diabetes_x_temp = diabetes.data[:, np.newaxis, 2]  #获取其中一个特征  
diabetes_x_train = diabetes_x_temp[:-20]           #训练样本  
diabetes_x_test = diabetes_x_temp[-20:]            #测试样本 后20行  
diabetes_y_train = diabetes.target[:-20]           #训练标记  
diabetes_y_test = diabetes.target[-20:]            #预测对比标记

#回归训练及预测  
clf = linear_model.LinearRegression()  
clf.fit(diabetes_x_train, diabetes_y_train)        #训练数据集  
pre = clf.predict(diabetes_x_test)

#绘图  
plt.title(u'LinearRegression Diabetes')            #标题  
plt.xlabel(u'Attributes')                          #x轴坐标  
plt.ylabel(u'Measure of disease')                  #y轴坐标    
plt.scatter(diabetes_x_test, diabetes_y_test, color = 'black')  #散点图   
plt.plot(diabetes_x_test, pre, color='blue', linewidth = 2)     #预测直线
plt.show()          
