#coding=utf-8
#By:Eastmount CSDN
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  
import lda
import numpy as np

#生成词频矩阵
corpus = []  
for line in open('test.txt', 'r').readlines():  
    corpus.append(line.strip())
vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(corpus)    
word = vectorizer.get_feature_names()

#LDA分布
model = lda.LDA(n_topics=3, n_iter=500, random_state=1)  
model.fit(X)

#文档-主题（Document-Topic）分布 
doc_topic = model.doc_topic_
print("shape: {}".format(doc_topic.shape))  
for n in range(9):  
    topic_most_pr = doc_topic[n].argmax()  
    print(u"文档: {} 主题: {}".format(n,topic_most_pr))  
