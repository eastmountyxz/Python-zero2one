import re
import urllib.request

url = "http://www.eastmountyxz.com/"
content = urllib.request.urlopen(url).read()
urls = re.findall(r'src="(.*?)"', content.decode('utf-8'))
for url in urls:
    print(url)
