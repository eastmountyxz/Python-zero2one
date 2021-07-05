# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
#载入数据集
from sklearn.datasets import load_boston
d = load_boston()
x = d.data
y = d.target
print(x[:2])
print('形状:', x.shape)

#降维
import numpy as np
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
newData = pca.fit_transform(x)
print('降维后数据:')
print(newData[:4])
print('形状:', newData.shape)
