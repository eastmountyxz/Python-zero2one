# -*- coding: utf-8 -*- 
#By:Eastmount CSDN
import numpy as np
import matplotlib.pyplot as plt

#随机产生4个整数(0到100之间)
data = np.random.randint(0,100,4) 
print(data)

ind = np.arange(4)  #四个用户
print(ind)
width = 0.35        #设置宽度      
x = ['UserA', 'UserB', 'UserC', 'UserD']

plt.bar(ind, data, width, color='green', label='Data')
plt.xlabel("Username")
plt.ylabel("Consumption")
plt.title("Compare four user monthly consumption data")
plt.legend()
plt.xticks(ind+width/2, x, rotation=40) #旋转40度
plt.show()

