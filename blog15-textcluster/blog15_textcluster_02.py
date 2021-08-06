#coding=utf-8
#By:Eastmount CSDN
import os  
import codecs
import jieba  
import jieba.analyse

source = open("test.txt", 'r')
line = source.readline().rstrip('\n')
content = []
while line!="":
    seglist = jieba.cut(line,cut_all=False)  #精确模式  
    output = ' '.join(list(seglist))         #空格拼接  
    print(output)
    content.append(output)
    line = source.readline().rstrip('\n')
else:
    source.close() 
