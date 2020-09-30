# coding=utf-8  
import re  
import urllib.request

url = "http://www.baidu.com/"  
content = urllib.request.urlopen(url).read()
pat = r'(?<=<title>).*?(?=</title>)'    
ex = re.compile(pat, re.M|re.S)
obj = re.search(ex, content.decode('utf-8'))
title = obj.group()  
print(title)
# 百度一下，你就知道
