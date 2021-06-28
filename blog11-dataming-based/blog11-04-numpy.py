#coding=utf-8
#By：Eastmount CSDN 2021-06-28
import numpy as np  

#调用sin函数和2的3次方  
print(np.sin(np.pi/6))
print(type(np.sin(0.5)))
f = np.power(2, 3)
print(f)

#范围定义  
print(np.arange(0,4))
print(type(np.arange(0,4)))

#调用求和函数、平均值函数、标准差函数
print(np.sum([1, 2, 3, 4]))
print(np.mean([4, 5, 6, 7]))
print(np.std([1, 2, 3, 2, 1, 3, 2, 0]))
