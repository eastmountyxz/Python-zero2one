# -*- coding: utf-8 -*-
import re 
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.eastmountyxz.com/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
essay0 = soup.find_all(attrs={"class":"essay"})
for tag in essay0:
    print(tag)
    print('')  #换行
    print(tag.a)
    print(tag.find("a").get_text())
    print(tag.find("a").attrs['href'])
    content = tag.find("p").get_text()
    print(content.replace(' ',''))
print('--------------------------\n')

#整理输出
i = 1
while i<=3:
    num = "essay" + str(i)
    essay = soup.find_all(attrs={"class":num})
    for tag in essay:
        print(tag.find("a").get_text())
        print(tag.find("a").attrs['href'])
        content = tag.find("p").get_text()
        print(content.replace(' ',''))
    i += 1
    print('')
