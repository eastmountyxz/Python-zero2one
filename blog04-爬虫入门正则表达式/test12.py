import re
import urllib.request

url = "http://www.eastmountyxz.com/"
content = urllib.request.urlopen(url).read()
title = re.findall(r'<title>(.*?)</title>', content.decode('utf-8'))
print(title[0])
