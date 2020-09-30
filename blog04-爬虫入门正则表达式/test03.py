# coding=utf-8
from urllib.parse import urlparse
url = urlparse('http://www.eastmount.com/index.asp?id=001')

print(url)          #url解析成六部分
print(url.netloc)   #输出网址
