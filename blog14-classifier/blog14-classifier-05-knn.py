# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-06
import numpy as np  
from sklearn.neighbors import KNeighborsClassifier  

X = np.array([[-1,-1],[-2,-2],[1,2], [1,1],[-3,-4],[3,2]])
Y = [0,0,1,1,0,1]
x = [[4,5],[-4,-3],[2,6]]
knn = KNeighborsClassifier(n_neighbors=3, algorithm="ball_tree")
knn.fit(X,Y)
pre = knn.predict(x)
print(pre)

distances, indices = knn.kneighbors(X)  
print(indices)
print(distances)
