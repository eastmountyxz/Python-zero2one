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

#计算个词语出现的次数
X = vectorizer.fit_transform(corpus)

#获取词袋中所有文本关键词 
word = vectorizer.get_feature_names()

print('特征个数:', len(word))
for n in range(len(word)):  
    print(word[n],end=" ")
print('')

#查看词频结果  
print(X.toarray())
