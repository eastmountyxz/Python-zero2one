# coding=utf-8  
import re
import urllib.request
content = urllib.request.urlopen("test.html").read() #打开本地文件

#获取<tr></tr>间内容
res = r'<tr>(.*?)</tr>'
texts = re.findall(res, content.decode('utf-8'), re.S|re.M)
for m in texts:
    print(m)

#获取<th></th>间内容
for m in texts:
    res_th = r'<th>(.*?)</th>'
    m_th = re.findall(res_th, m, re.S|re.M)
    for t in m_th:
        print(t)

#直接获取<td></td>间内容
res = r'<td>(.*?)</td><td>(.*?)</td>'    
texts = re.findall(res, content.decode('utf-8'), re.S|re.M)
for m in texts:
    print(m[0],m[1])
