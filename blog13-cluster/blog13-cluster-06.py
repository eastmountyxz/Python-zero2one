# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn.cluster import Birch
X = [[1,1],[2,1],[1,3],[6,6],[8,5],[7,8]]
y = [0,0,0,1,1,1]
clf = Birch(n_clusters=2)
clf.fit(X,y)
print(clf.labels_)
