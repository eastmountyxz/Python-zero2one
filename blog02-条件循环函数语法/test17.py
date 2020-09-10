# -*- coding:utf-8 -*-
#字符串库函数
str1 = "hello world"
print('计算字符串长度:', len(str1))
str2 = str1.title()
print('首字母大写标题转换:', str2)
str3 = '12ab34ab56ab78ab'
print('字符串替换:', str3.replace('ab',' '))

#数学库函数
import math
print(math.pi)
num1 = math.cos(math.pi/3)
print('余弦定律:', num1)
num2 = pow(2,10)
print('幂次运算:', num2)
num3 = math.log10(1000)
print('求以10为底的对数:', num3)

#操作系统库函数
import os
print('输出当前使用平台:', os.name)
path = os.getcwd()
print('获取当前工作目录', path)
os.system('taskkill /F /IM iexplore.exe') #关闭浏览器进程

#网络套接字库函数
import socket
ip = socket.gethostbyname('www.baidu.com')
print('获取百度ip地址', ip)
