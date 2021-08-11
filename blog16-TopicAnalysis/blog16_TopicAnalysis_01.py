#coding=utf-8
#By:Eastmount CSDN
import jieba  
import sys  
import matplotlib.pyplot as plt  
from wordcloud import WordCloud  

text = open('test.txt').read()  
print(type(text)) 
wordlist = jieba.cut(text, cut_all = True)  
wl_space_split = " ".join(wordlist)  
print(wl_space_split)   
my_wordcloud = WordCloud().generate(wl_space_split)   
plt.imshow(my_wordcloud)   
plt.axis("off")  
plt.show()
