#coding=utf-8
#By:Eastmount CSDN
import jieba  
  
text = "小杨毕业于北京理工大学，从事Python人工智能相关工作。"  

#全模式
data = jieba.cut(text,cut_all=True)
print(type(data))
print(u"[全模式]: ", "/".join(data))

#精确模式  
data = jieba.cut(text,cut_all=False)
print(u"[精确模式]: ", "/".join(data))

#默认是精确模式 
data = jieba.cut(text)  
print(u"[默认模式]: ", "/".join(data))

#搜索引擎模式 
data = jieba.cut_for_search(text)    
print(u"[搜索引擎模式]: ", "/".join(data))

#返回列表
seg_list = jieba.lcut(text, cut_all=False)
print("[返回列表]: {0}".format(seg_list))
