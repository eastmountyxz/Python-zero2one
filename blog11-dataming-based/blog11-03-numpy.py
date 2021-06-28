#coding=utf-8
#By：Eastmount CSDN 2021-06-28

#定义二维数组  
import numpy as np  
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

print('形状:', c.shape)
print('获取值:', c[1][0])
print('获取某行:')
print(c[1][:])
print('获取某行并切片:')
print(c[0][:-1])
print(c[0][-1:]) 
