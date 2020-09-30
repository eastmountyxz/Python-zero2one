# coding=utf-8
import urllib.parse
url = urllib.parse.urlparse('http://www.eastmount.com/index.asp?id=001')

print(url)           #url解析成六部分
print(url.netloc)    #输出网址

#重组URL
u = urllib.parse.urlunparse(url)
print(u)
