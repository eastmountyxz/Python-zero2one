# coding=utf-8
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('test04_01.html'), "html.parser")
print(soup.head.contents)
#['\n', <title>BeautifulSoup技术</title>, '\n']

print(soup.head.contents[1])
#<title>BeautifulSoup技术</title>

for child in soup.descendants:
    print(child)

for content in soup.stripped_strings:
    print(content)

#搜索文档树
urls = soup.find_all('a')
for u in urls:
    print(u)
