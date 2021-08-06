#coding:utf-8
#By:Eastmount CSDN
from sklearn.feature_extraction.text import CountVectorizer  
  
#存储读取语料 一行预料为一个文档
corpus = []  
for line in open('result.txt', 'r', encoding="utf-8").readlines():  
    corpus.append(line.strip())
    
#将文本中的词语转换为词频矩阵  
vectorizer = CountVectorizer()

#计算个词语出现的次数  
X = vectorizer.fit_transform(corpus)

#获取词袋中所有文本关键词  
word = vectorizer.get_feature_names()  
for n in range(len(word)):  
    print(word[n],end=" ")
print('')
    
#查看词频结果  
print(X.toarray())
