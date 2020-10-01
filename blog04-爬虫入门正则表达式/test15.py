import re
import urllib.request

url = "http://www.eastmountyxz.com/"
content = urllib.request.urlopen(url).read()
data = content.decode('utf-8')

start = data.find(r'<div class="essay">')
end = data.find(r'<div class="essay1">')
page = data[start:end]
                 
res = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
t1 = re.findall(res, page) #超链接
print(t1[0])
t2 = re.findall(r'<a .*?>(.*?)</a>', page)  #标题
print(t2[0])
t3 = re.findall('<p style=.*?>(.*?)</p>', page, re.M|re.S) #摘要
print(t3[0])
