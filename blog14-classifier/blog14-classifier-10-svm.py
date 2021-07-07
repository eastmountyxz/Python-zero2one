# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-06
import os 
import numpy as np
from sklearn.svm import SVC  
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

#第一步 加载数据集
path = "wine/wine.txt"
data = np.loadtxt(path,dtype=float,delimiter=",")
print(data)

#第二步 划分数据集
yy, x = np.split(data, (1,), axis=1) #第一列类标yy,后面13列特征为x
print(yy.shape, x.shape)
y = []
for n in yy: 
    y.append(int(n))
y =  np.array(y, dtype = int) #list转换数组
#划分数据集 测试集40%
train_data, test_data, train_target, test_target = train_test_split(x, y, test_size=0.4, random_state=42)
print(train_data.shape, train_target.shape)
print(test_data.shape, test_target.shape)

#第三步 SVC训练
clf = SVC()
clf.fit(train_data, train_target)
result = clf.predict(test_data)
print(result)
print(test_target)

#第四步 评价算法 
print(sum(result==test_target))                            #预测结果与真实结果比对
print(metrics.classification_report(test_target, result))  #准确率 召回率 F值

#第五步 降维操作
pca = PCA(n_components=2)      
newData = pca.fit_transform(test_data)
                  
#第六步 绘图可视化
plt.figure()
cmap_bold = ListedColormap(['#000000', '#00FF00', '#FFFFFF'])
plt.scatter(newData[:,0], newData[:,1], c=test_target, cmap=cmap_bold, s=50)
plt.show()
