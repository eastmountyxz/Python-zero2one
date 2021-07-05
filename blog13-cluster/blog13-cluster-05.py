# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03

#------------------------------------------------------------------------
#第一步 读取数据
import os

data = []
for line in open("data.txt", "r").readlines():  
    line = line.rstrip()    
    result = ' '.join(line.split())
    #将字符串转换为小数  
    s = [float(x) for x in result.strip().split(' ')]  
    print(s)  
    data.append(s)
print(data) 
print(type(data))

#------------------------------------------------------------------------
#第二步 获取两列数据
print('第一列 第五列数据')  
L2 = [n[0] for n in data]  #第一列表示球员每分钟助攻数：assists_per_minute  
L5 = [n[4] for n in data]  #第五列表示球员每分钟得分数：points_per_minute    
T = dict(zip(L2,L5))       #两列数据生成二维数据
type(T)
print(L2)

#下述代码将dict类型转换为list    
X = list(map(lambda x,y: (x,y), T.keys(),T.values()))  
print(type(X)) 
print(X)

#------------------------------------------------------------------------
#第三步 聚类分析
from sklearn.cluster import KMeans 
clf = KMeans(n_clusters=3)  
y_pred = clf.fit_predict(X)  
print(clf)   
print(y_pred)

#------------------------------------------------------------------------
#第四步 绘制图形
import numpy as np  
import matplotlib.pyplot as plt  

#获取第一列和第二列数据，使用for循环获取，n[0]表示X第一列  
x = [n[0] for n in X]  
y = [n[1] for n in X]

#坐标  
x1, y1 = [], []   
x2, y2 = [], [] 
x3, y3 = [], []   
  
#分布获取类标为0、1、2的数据并赋值给(x1,y1) (x2,y2) (x3,y3)  
i = 0  
while i < len(X):  
    if y_pred[i]==0:  
        x1.append(X[i][0])  
        y1.append(X[i][1])  
    elif y_pred[i]==1:  
        x2.append(X[i][0])
        y2.append(X[i][1])  
    elif y_pred[i]==2:  
        x3.append(X[i][0])  
        y3.append(X[i][1])  
    i = i + 1  
  
#三种颜色 红 绿 蓝，marker='x'表示类型，o表示圆点、*表示星型、x表示点   
plot1, = plt.plot(x1, y1, 'or', marker="x")    
plot2, = plt.plot(x2, y2, 'og', marker="o")    
plot3, = plt.plot(x3, y3, 'ob', marker="*")    
  
plt.title("Kmeans-Basketball Data")  #绘制标题
plt.xlabel("assists_per_minute")     #绘制x轴 
plt.ylabel("points_per_minute")      #绘制y轴
plt.legend((plot1, plot2, plot3), ('A', 'B', 'C'), fontsize=10)    #设置右上角图例  

#------------------------------------------------------------------------
#第五步 设置类簇中心 
centers = clf.cluster_centers_
print(centers)
plt.plot(centers[:,0],centers[:,1],'r*',markersize=20)  #显示三个中心点
plt.show()  
