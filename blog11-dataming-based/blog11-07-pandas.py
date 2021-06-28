#coding=utf-8
#By：Eastmount CSDN 2021-06-28
from pandas import Series, DataFrame

a = Series([4, 7, -5, 3])  
print('创建Series:')
print(a)   

b = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  
print('创建带有索引的Series:')
print(b) 

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}  
c = Series(sdata)  
print('通过传递字典创建Series:')
print(c)  

states = ['California', 'Ohio', 'Oregon', 'Texas']  
d = Series(sdata, index=states)  
print('California没有字典为空:')
print(d)  
