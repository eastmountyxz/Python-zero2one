# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import matplotlib.pyplot as plt
import numpy as np

num = np.array([1342, 6092, 4237, 8219])   #数量
ratio = np.array([0.75, 0.76, 0.72, 0.75]) #男性占比
men = num * ratio
women = num * (1-ratio)
x = ['学习',u'旅游',u'看剧',u'聊天']

plt.rc('font', family='SimHei', size=13)   #中文字体显示

width = 0.5
idx = np.arange(4)
plt.bar(idx, men, width, color='red', label='男性用户')
plt.bar(idx, women, width, bottom=men, color='yellow', label='女性用户')
plt.xticks(idx+width/2, x, rotation=40)
plt.legend()
plt.show()
