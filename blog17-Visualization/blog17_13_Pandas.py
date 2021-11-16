# -*- coding: utf-8 -*-
#By:Eastmount CSDN
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv",index_col='year')    
plt.rcParams['font.sans-serif'] = ['simHei']
plt.rcParams['axes.unicode_minus'] = False

#获取贵阳数据集并绘图 
gy = data['Guiyang']  
print(gy, type(gy))
gy.plot()
data['Beijing'].plot(color='r')
plt.show()  
