import re
import urllib.request
url = "http://www.eastmountyxz.com/"
content = urllib.request.urlopen(url).read()
data = content.decode('utf-8')
start = data.find(r'<div class="essay">')
end = data.find(r'<div class="essay1">')
print(data[start:end])
