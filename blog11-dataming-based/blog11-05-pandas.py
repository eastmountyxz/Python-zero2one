#coding=utf-8
#By：Eastmount CSDN 2021-06-28
import pandas as pd

#读取数据，其中参数header设置Excel无标题头
data = pd.read_excel("data.xls", header=None) 
print(data)

#计算数据长度
print('行数', len(data))

#计算用户A\B\C消费求和
print(data.sum())

#计算用户A\B\C消费算术平均数
mm = data.sum()
print(mm)

#输出预览前5行数据
print('预览前5行数据')
print(data.head())
