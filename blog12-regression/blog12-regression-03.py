# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn import datasets
diabetes = datasets.load_diabetes()                           #载入数据  
print(diabetes.data)                                          #数据  
print(diabetes.target)                                        #类标  
print('总行数: ', len(diabetes.data), len(diabetes.target))         
print('特征数: ', len(diabetes.data[0]))                      #每行数据集维数  
print('数据类型: ', diabetes.data.shape)                     
print(type(diabetes.data), type(diabetes.target))     
