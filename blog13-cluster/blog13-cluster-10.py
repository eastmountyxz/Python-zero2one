# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
#第一步 数据获取
import pandas as pd
glass = pd.read_csv("glass.csv")
print(glass[:4])

#第二步 聚类
from sklearn.cluster import Birch
clf = Birch(n_clusters=3)
clf.fit(glass)
pre = clf.predict(glass)
print(pre)

#第三步 降维
from sklearn.decomposition import PCA  
pca = PCA(n_components=2)  
newData = pca.fit_transform(glass)  
print(newData[:4])
x1 = [n[0] for n in newData]  
x2 = [n[1] for n in newData]

#第四步 绘图
import matplotlib.pyplot as plt
plt.xlabel("x feature")  
plt.ylabel("y feature")  
plt.scatter(x1, x2, c=pre, marker='x')   
plt.show()  
