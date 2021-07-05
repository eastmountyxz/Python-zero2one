# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import Birch

#数据获取
glass=pd.read_csv("glass.csv")
X1 = glass.al
X2 = glass.ri
T = dict(zip(X1,X2)) #生成二维数组   
X = list(map(lambda x,y: (x,y), T.keys(),T.values())) #dict类型转换为list 
y = glass.glass_type

#聚类
clf = Birch(n_clusters=3)
clf.fit(X, y)
y_pred = clf.predict(X)
print(y_pred)

#分别获取不同类别数据点 
x1, y1 = [], []   
x2, y2 = [], [] 
x3, y3 = [], []
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
  
#三种颜色 红 绿 蓝，marker='x'表示类型，o表示圆点 *表示星型 x表示点   
plot1, = plt.plot(x1, y1, 'or', marker="x")    
plot2, = plt.plot(x2, y2, 'og', marker="o")    
plot3, = plt.plot(x3, y3, 'ob', marker="*")
plt.xlabel('al')
plt.ylabel('ri')
plt.show()
