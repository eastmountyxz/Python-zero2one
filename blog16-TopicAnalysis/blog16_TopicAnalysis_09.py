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
    print(u"文档: {} 主题: {}".format(n+1,topic_most_pr))
topic_word = model.topic_word_

#可视化分析
import matplotlib.pyplot as plt
f, ax= plt.subplots(3, 1, figsize=(8,6), sharex=True) #三个主题
for i, k in enumerate([0, 1, 2]):
    ax[i].stem(topic_word[k,:], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-1, 43)      #单词43个
    ax[i].set_ylim(0, 0.5)      #单词出现频率
    ax[i].set_ylabel("y")
    ax[i].set_title("Topic {}".format(k))
ax[1].set_xlabel("word")
plt.tight_layout()
plt.savefig("result2.png")
plt.show() 
