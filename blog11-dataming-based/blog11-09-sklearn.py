#coding=utf-8
#By：Eastmount CSDN 2021-06-28
from sklearn.cluster import KMeans

X = [[1],[2],[3],[4],[5]]
y = [4,2,6,1,3]
clf = KMeans(n_clusters=2)
clf.fit(X,y)
print(clf)
print(clf.labels_) 
