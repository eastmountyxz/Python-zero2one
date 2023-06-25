# -*- coding: utf-8 -*-  
# By:Eastmount CSDN 2021-07-06
import os 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier  
from sklearn import metrics
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#----------------------------------------------------------------------------
#第一步 加载数据集
path = "wine/wine.data"
data = np.loadtxt(path,dtype=float,delimiter=",")
print(data)

#----------------------------------------------------------------------------
#第二步 划分数据集
yy, x = np.split(data, (1,), axis=1) #第一列为类标yy,后面13列特征为x
print(yy.shape, x.shape)
y = []
for n in yy:  #将类标浮点型转化为整数
    y.append(int(n))
x = x[:, :2]  #获取x前两列数据,方便绘图 对应x、y轴
train_data = np.concatenate((x[0:40,:], x[60:100,:], x[140:160,:]), axis = 0)  #训练集
train_target = np.concatenate((y[0:40], y[60:100], y[140:160]), axis = 0)      #样本类别
test_data = np.concatenate((x[40:60, :], x[100:140, :], x[160:,:]), axis = 0)  #测试集
test_target = np.concatenate((y[40:60], y[100:140], y[160:]), axis = 0)        #样本类别
print(train_data.shape, train_target.shape)
print(test_data.shape, test_target.shape)

#----------------------------------------------------------------------------
#第三步 KNN训练
clf = KNeighborsClassifier(n_neighbors=3,algorithm='kd_tree') #K=3
clf.fit(train_data,train_target)
result = clf.predict(test_data)
print(result)

#----------------------------------------------------------------------------
#第四步 评价算法 
print(sum(result==test_target))                             #预测结果与真实结果比对
print(metrics.classification_report(test_target, result))   #准确率 召回率 F值

#----------------------------------------------------------------------------
#第五步 创建网格
x1_min, x1_max = test_data[:,0].min()-0.1, test_data[:,0].max()+0.1    #第一列
x2_min, x2_max = test_data[:,1].min()-0.1, test_data[:,1].max()+0.1    #第二列
xx, yy = np.meshgrid(np.arange(x1_min, x1_max, 0.1),  
                     np.arange(x2_min, x2_max, 0.1))                   #生成网格型数据
print(xx.shape, yy.shape)                                               #(53L, 36L) (53L, 36L)

z = clf.predict(np.c_[xx.ravel(), yy.ravel()])                         #ravel()拉直函数
print(xx.ravel().shape, yy.ravel().shape)                              #(1908L,) (1908L,)
print(np.c_[xx.ravel(), yy.ravel()].shape)                             #合并 (1908L,2)

#----------------------------------------------------------------------------
#第六步 绘图可视化
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])         #颜色Map
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
plt.figure()
z = z.reshape(xx.shape)
print(xx.shape, yy.shape, z.shape, test_target.shape)                 
#(53L, 36L) (53L, 36L) (53L, 36L)  (78L,)
plt.pcolormesh(xx, yy, z, cmap=cmap_light)
plt.scatter(test_data[:,0], test_data[:,1], c=test_target,
            cmap=cmap_bold, s=50)
plt.show()
