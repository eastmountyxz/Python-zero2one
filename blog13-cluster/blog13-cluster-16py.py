# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
import os
import codecs
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import jieba
from sklearn import metrics
from sklearn.metrics import silhouette_score
from array import array
from numpy import *
from pylab import mpl
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.cluster.hierarchy import ward, dendrogram

#---------------------------------------加载语料-------------------------------------
text = open('data-fenci.txt').read()
print(text)
list1=text.split("\n")
print(list1)
print(list1[0])
print(list1[1])
mytext_list=list1

#控制显示数量
count_vec = CountVectorizer(min_df=20, max_df=1000)  #最大值忽略
xx1 = count_vec.fit_transform(list1).toarray()
word=count_vec.get_feature_names() 
print("word feature length: {}".format(len(word)))
print(word)
print(xx1)
print(type(xx1))
print(xx1.shape)
print(xx1[0])

#---------------------------------------层次聚类-------------------------------------
titles = word
#dist = cosine_similarity(xx1)

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.DataFrame(xx1)
print(df.corr())
print(df.corr('spearman'))
print(df.corr('kendall'))
dist = df.corr()
print (dist)
print(type(dist))
print(dist.shape)

#define the linkage_matrix using ward clustering pre-computed distances
linkage_matrix = ward(dist) 
fig, ax = plt.subplots(figsize=(8, 12)) # set size
ax = dendrogram(linkage_matrix, orientation="right",
                p=20, labels=titles, leaf_font_size=12
                ) #leaf_rotation=90., leaf_font_size=12.
#show plot with tight layout
plt.tight_layout() 
#save figure as ward_clusters
plt.savefig('KH.png', dpi=200)
plt.show()
