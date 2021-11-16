# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import pandas as pd
import matplotlib.pyplot as plt

#读取文件并显示前6行数据 index_col用作行索引的列名
data = pd.read_csv("data.csv",index_col='year')   
print(data.shape)  
print(data.head(6))  

plt.rcParams['font.sans-serif'] = ['simHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号

data.plot()
plt.savefig(u'test16.png', dpi=500)
plt.show()
