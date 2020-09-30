# coding=utf-8  
import re  
import urllib.request
url = "http://www.baidu.com/"  
content = urllib.request.urlopen(url).read()

#获取完整超链接
res = r"<a.*?href=.*?<\/a>"
urls = re.findall(res, content.decode('utf-8'))
for u in urls:
    print(u)

#获取超链接<a>和</a>之间内容
res = r'<a .*?>(.*?)</a>'  
texts = re.findall(res, content.decode('utf-8'), re.S|re.M)  
for t in texts:
    print(t)
