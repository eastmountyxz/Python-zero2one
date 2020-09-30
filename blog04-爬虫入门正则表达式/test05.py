# coding=utf-8  
import re  
import urllib.request
url = "http://www.baidu.com/"  
content = urllib.request.urlopen(url).read()
title = re.findall(r'<title>(.*?)</title>', content.decode('utf-8'))
print(title[0])
# 百度一下，你就知道
