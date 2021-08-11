#coding=utf-8
#By:Eastmount CSDN
import jieba  
  
#全模式  
text = "我来到北京清华大学"  
seg_list = jieba.cut(text, cut_all=True)  
print("[全模式]: ", "/ ".join(seg_list))
#[全模式]: 我 / 来到 / 北京 / 清华 / 清华大学 / 华大 /大学
  
#精确模式  
seg_list = jieba.cut(text, cut_all=False)  
print("[精确模式]: ", "/ ".join(seg_list))
#[精确模式]: 我 / 来到 / 北京 / 清华大学
  
#默认是精确模式  
seg_list = jieba.cut(text)  
print("[默认模式]: ", "/ ".join(seg_list)) 
#[默认模式]: 我 / 来到 / 北京 / 清华大学 
 
 #搜索引擎模式  
seg_list = jieba.cut_for_search(text)   
print("[搜索引擎模式]: ", "/ ".join(seg_list))
#[搜索引擎模式]: 我 / 来到 / 北京 / 清华 / 华大 / 大学 / 清华大学 
