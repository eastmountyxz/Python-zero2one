# coding:utf-8
#By:Eastmount CSDN
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  
  
#第一步 生成词频矩阵
corpus = []  
for line in open('result.txt', 'r', encoding="utf-8").readlines():  
    corpus.append(line.strip())
vectorizer = CountVectorizer() 
X = vectorizer.fit_transform(corpus) 
word = vectorizer.get_feature_names()    
for n in range(len(word)):  
    print(word[n],end=" ")
print('')  
print(X.toarray())

#第二步 计算TF-IDF值
transformer = TfidfTransformer()  
print(transformer)
tfidf = transformer.fit_transform(X)
print(tfidf.toarray())
weight = tfidf.toarray()

#第三步 KMeans聚类
from sklearn.cluster import KMeans  
clf = KMeans(n_clusters=3)  
s = clf.fit(weight) 
y_pred = clf.fit_predict(weight)
print(clf)
print(clf.cluster_centers_) #类簇中心
print(clf.inertia_)         #距离:用来评估簇的个数是否合适 越小说明簇分的越好
print(y_pred)               #预测类标

#第四步 降维处理
from sklearn.decomposition import PCA  
pca = PCA(n_components=2)   #降低成两维绘图 
newData = pca.fit_transform(weight)  
print(newData)
x = [n[0] for n in newData]  
y = [n[1] for n in newData]  

#第五步 可视化
import numpy as np  
import matplotlib.pyplot as plt   
plt.scatter(x, y, c=y_pred, s=100, marker='s')  
plt.title("Kmeans")    
plt.xlabel("x")  
plt.ylabel("y")    
plt.show() 

