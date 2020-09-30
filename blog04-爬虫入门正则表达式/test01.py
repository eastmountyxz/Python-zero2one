# -*- coding:utf-8 -*-
import urllib.request
import webbrowser as web  

url = "http://www.baidu.com"
content = urllib.request.urlopen(url)

print(content.info())     #头信息
print(content.geturl())   #请求url
print(content.getcode())  #http状态码

#保存网页至本地并通过浏览器打开
open("baidu.html","wb").write(content.read())
web.open_new_tab("baidu.html")
