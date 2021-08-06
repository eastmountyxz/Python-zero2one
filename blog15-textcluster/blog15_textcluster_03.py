#coding=utf-8
#By:Eastmount CSDN
import os  
import codecs
import jieba  
import jieba.analyse

#停用词表
stopwords = {}.fromkeys(['的', '或', '等', '是', '有', '之', '与',
                         '和', '也', '被', '吗', '于', '中', '最'])

source = open("test.txt", 'r')
line = source.readline().rstrip('\n')
content = []                                 #完整文本

while line!="":
    seglist = jieba.cut(line,cut_all=False)  #精确模式
    final = []                               #存储去除停用词内容
    for seg in seglist: 
        if seg not in stopwords:  
            final.append(seg)
    output = ' '.join(list(final))           #空格拼接
    print(output)
    content.append(output)
    line = source.readline().rstrip('\n')
else:
    source.close()
