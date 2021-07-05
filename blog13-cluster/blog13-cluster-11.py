# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import Birch

#获取数据集及降维
glass = pd.read_csv("glass.csv")
pca = PCA(n_components=2)  
newData = pca.fit_transform(glass)  
print(newData[:4]) 
L1 = [n[0] for n in newData]  
L2 = [n[1] for n in newData]
plt.rc('font', family='SimHei', size=8) #设置字体
plt.rcParams['axes.unicode_minus'] = False #负号

#聚类 类簇数=2
clf = Birch(n_clusters=2)
clf.fit(glass)
pre = clf.predict(glass)
p1 = plt.subplot(221)  
plt.title(u"Birch聚类 n=2")  
plt.scatter(L1,L2,c=pre,marker="s")  
plt.sca(p1)  

#聚类 类簇数=3
clf = Birch(n_clusters=3)
clf.fit(glass)
pre = clf.predict(glass)
p2 = plt.subplot(222)  
plt.title(u"Birch聚类 n=3")  
plt.scatter(L1,L2,c=pre,marker="o")
plt.sca(p2)  

#聚类 类簇数=4
clf = Birch(n_clusters=4)
clf.fit(glass)
pre = clf.predict(glass)
p3 = plt.subplot(223)  
plt.title(u"Birch聚类 n=4")  
plt.scatter(L1,L2,c=pre,marker="o")
plt.sca(p3)  

#聚类 类簇数=5
clf = Birch(n_clusters=5)
clf.fit(glass)
pre = clf.predict(glass)
p4 = plt.subplot(224)  
plt.title(u"Birch聚类 n=5")  
plt.scatter(L1,L2,c=pre,marker="s")
plt.sca(p4)  
plt.savefig('18.20.png', dpi=300) 
plt.show()  
