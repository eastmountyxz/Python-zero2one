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
    value0 = m[0].replace('<br />', '').replace('&nbsp;', '')
    value1 = m[1].replace('<br />', '').replace('&nbsp;', '')
    if '<B>' in value1:
        m_value = re.findall(r'<B>(.*?)</B>', value1, re.S|re.M)
        print(value0, m_value[0])
    else:
        print(value0, value1)
