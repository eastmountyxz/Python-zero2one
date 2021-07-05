# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn.cluster import KMeans
X = [[1,1],[2,1],[1,3],[6,6],[8,5],[7,8]]
y = [0,0,0,1,1,1]
clf = KMeans(n_clusters=2)
clf.fit(X,y)
print(clf)
print(clf.labels_)

import matplotlib.pyplot as plt
a = [n[0] for n in X]  
b = [n[1] for n in X]
plt.scatter(a, b, c=clf.labels_)
plt.show()
