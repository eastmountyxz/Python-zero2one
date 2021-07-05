# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
print(pca)
pca.fit(X)
print(pca.explained_variance_ratio_) 
