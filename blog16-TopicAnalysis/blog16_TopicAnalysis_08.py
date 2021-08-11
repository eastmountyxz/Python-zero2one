#coding=utf-8
#By:Eastmount CSDN 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  
import lda
import numpy as np

#生词频矩阵
corpus = []  
for line in open('test.txt', 'r').readlines():  
    corpus.append(line.strip())
vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(corpus)  
  
#LDA分布
model = lda.LDA(n_topics=3, n_iter=500, random_state=1)  
model.fit_transform(X)

#文档-主题（Document-Topic）分布 
doc_topic = model.doc_topic_
print("shape: {}".format(doc_topic.shape))  
for n in range(9):  
    topic_most_pr = doc_topic[n].argmax()  
    print("文档: {} 主题: {}".format(n+1,topic_most_pr))
    
#可视化分析
import matplotlib.pyplot as plt  
f, ax= plt.subplots(9, 1, figsize=(10, 10), sharex=True)  
for i, k in enumerate([0,1,2,3,4,5,6,7,8]):  
    ax[i].stem(doc_topic[k,:], linefmt='r-',  
               markerfmt='ro', basefmt='w-')  
    ax[i].set_xlim(-1, 3)      #三个主题
    ax[i].set_ylim(0, 1.0)     #权重0-1之间
    ax[i].set_ylabel("y")  
    ax[i].set_title("Document {}".format(k+1))  
ax[4].set_xlabel("Topic")  
plt.tight_layout()
plt.savefig("result.png")
plt.show() 
