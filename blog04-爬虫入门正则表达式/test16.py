#coding:utf-8
import re
import urllib.request

url = "http://www.eastmountyxz.com/"
content = urllib.request.urlopen(url).read()
data = content.decode('utf-8')

#爬取标题
title = re.findall(r'<title>(.*?)</title>', data)
print(title[0])

#爬取图片地址
urls = re.findall(r'src="(.*?)"', data)
for url in urls:
    print(url)

#爬取内容
start = data.find(r'<div class="essay">')
end = data.find(r'<div class="essay1">')
page = data[start:end]           
res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
t1 = re.findall(res, page)  #超链接
print(t1[0])
t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
print(t2[0])
t3 = re.findall('<p style=.*?>(.*?)</p>', page, re.M|re.S) #摘要
print(t3[0])
print('')

start = data.find(r'<div class="essay1">')
end = data.find(r'<div class="essay2">')
page = data[start:end]           
res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
t1 = re.findall(res, page)  #超链接
print(t1[0])
t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
print(t2[0])
t3 = re.findall('<p style=.*?>(.*?)</p>', page, re.M|re.S) #摘要
print(t3[0])


