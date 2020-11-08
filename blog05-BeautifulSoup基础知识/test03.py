# coding=utf-8
from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="test" id="yxz">Eastmount</b>',"html.parser")
tag = soup.b
print(tag)
print(type(tag))

#Name
print(tag.name)
print(tag.string)

#Attributes
print(tag.attrs)
print(tag['class'])
print(tag.get('id'))

#修改属性 增加属性name
tag['class'] = 'abc'
tag['id'] = '1'
tag['name'] = '2'
print(tag)

#删除属性
del tag['class']
del tag['name']
print(tag)
print(tag['class'])
#KeyError: 'class'
