# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import matplotlib.pyplot as plt

#每一块占得比例，总和为100
mm = [45, 30, 25]             
n = mm[0]+mm[1]+mm[2]
a = (mm[0]*1.0*100/n)
b = (mm[1]*1.0*100/n)
c = (mm[2]*1.0*100/n)
fracs = [a, b, c]
print(a, b, c, n)

#离开整体的距离
explode=(0, 0, 0.08)
labels = 'A', 'B', 'C'

#绘制图形
plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors = ("c", "r", "y"))
plt.show()
