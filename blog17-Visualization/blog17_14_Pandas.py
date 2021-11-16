# -*- coding: utf-8 -*-
#By:Eastmount CSDN
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", index_col='year')    
plt.rcParams['font.sans-serif'] = ['simHei']
plt.rcParams['axes.unicode_minus'] = False 

#在图表中创建子图 4个子图
p1 = plt.subplot(221)   
data['Beijing'].plot(color='r', kind='bar')
plt.sca(p1)

p2 = plt.subplot(222)   
data['Guiyang'].plot(color='y', kind='barh')
plt.sca(p2)

p3 = plt.subplot(223)
data.Shanghai.plot(kind='line')
plt.sca(p3)

p4 = plt.subplot(224)   
data['Changsha'].plot(kind='kde')
plt.sca(p4)
plt.show()

data.plot(color='y', kind='bar', subplots=True)
plt.show()
