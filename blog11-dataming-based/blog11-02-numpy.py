#coding=utf-8
#By：Eastmount CSDN 2021-06-28

#导入包并重命名np
import numpy as np

#定义一维数组
a = np.array([2, 0, 1, 5, 8, 3])
print('原始数据:', a)

#输出最大、最小值及形状
print('最小值:', a.min())
print('最大值:', a.max())
print('形状', a.shape)

#数据切片
print('切片操作:')
print(a[:-2])
print(a[-2:])
print(a[:1])

#排序  
print(type(a)) 
a.sort()  
print('排序后:', a)
# <type 'numpy.ndarray'>  
# 排序后: [0 1 2 3 5 8] 
