# coding=utf-8
from bs4 import BeautifulSoup

#创建本地文件soup对象
soup = BeautifulSoup(open('test04_01.html'), "html.parser")

#获取标题
title = soup.title
print('标题:', title)

#获取标题
head = soup.head
print('头部:', head)

#获取a标签
ta = soup.a
print('超链接内容:', ta)

#获取p标签
tp = soup.p
print('段落内容:', tp)

#从文档中找到<a>的所有标签链接
for a in soup.find_all('a'):
    print(a)

#获取<a>的超链接
for link in soup.find_all('a'):  
    print(link.get('href'))

print(soup.title)
# <title>BeautifulSoup技术</title>
print(soup.head)
# <head><title>BeautifulSoup技术</title></head>
print(soup.p)
# <p class="title"><b>静夜思</b></p>
print(soup.a)
# <a class="poet" href="http://example.com/dufu" id="link1">杜甫</a>

print(soup.name)
#[document]
print(soup.head.name)
#head
print(soup.title.name)
#title
