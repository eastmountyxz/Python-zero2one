# coding=utf-8  
import re

content = '''
<tr><td>1001</td><td>杨秀璋<br /></td></tr>
<tr><td>1002</td><td>颜&nbsp;娜</td></tr>
<tr><td>1003</td><td><B>Python</B></td></tr>
'''

res = r'<td>(.*?)</td><td>(.*?)</td>'    
texts = re.findall(res, content, re.S|re.M)
for m in texts:
    print(m[0],m[1])
