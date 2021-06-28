#coding=utf-8
#By：Eastmount CSDN 2021-06-28
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", header=None) 
print(data)
mm = data.sum()  #求和
print(mm[1:])    #第一列为序号,取后面三列值

ind = np.arange(3)  #3个用户 0 1 2    
width = 0.35       #设置宽度          
x = [u'用户A', u'用户B', u'用户C']
plt.rc('font', family='SimHei', size=13) #中文字体显示 

#绘图  
plt.bar(ind, mm[1:], width, color='r', label='sum num')  
plt.xlabel(u"用户")  
plt.ylabel(u"消费数据")  
plt.title(u"用户消费数据对比柱状图")  
plt.legend()  
#设置底部名称  
plt.xticks(ind+width/2, x, rotation=40) #旋转40度  
plt.show()  
