# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn.cluster import MiniBatchKMeans
X= [[1],[2],[3],[4],[3],[2]]
mbk = MiniBatchKMeans(init='k-means++', n_clusters=3, n_init=10)
clf = mbk.fit(X)
print(clf.labels_)
#输出：[0 2 1 1 1 2]

from sklearn.cluster import Birch
X = [[1],[2],[3],[4],[3],[2]]
clf = Birch(n_clusters=2)
clf.fit(X)
y_pred = clf.fit_predict(X)
print(clf)
print(y_pred)
#输出：[1 1 0 0 0 1]
