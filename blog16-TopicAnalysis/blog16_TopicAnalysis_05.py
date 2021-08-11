#coding=utf-8
#By:Eastmount CSDN
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  
  
#读取语料
corpus = []  
for line in open('test.txt', 'r').readlines():  
    corpus.append(line.strip())
    
#将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(corpus)  #计算个词语出现的次数  
word = vectorizer.get_feature_names() #获取词袋中所有文本关键词
print('特征个数:', len(word))
for n in range(len(word)):  
    print(word[n],end=" ")
print('')  
print(X.toarray())                    #查看词频结果 

#计算TF-IDF值
transformer = TfidfTransformer()  
print(transformer)
tfidf = transformer.fit_transform(X) #将词频矩阵X统计成TF-IDF值

#查看数据结构 输出tf-idf权重
print(tfidf.toarray())
weight = tfidf.toarray()
