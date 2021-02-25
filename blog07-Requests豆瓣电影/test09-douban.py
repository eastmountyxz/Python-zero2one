# coding:utf-8
# By:Eastmount 2021-02-25
import requests
from lxml import etree

#设置浏览器代理,它是一个字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url = 'https://movie.douban.com/top250?start=0&filter='

#向服务器发出请求
r = requests.get(url = url, headers = headers).text

#解析DOM树结构
html_etree = etree.HTML(r)
name = html_etree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
print ("这是数组形式：",name)
print ("这是字符串形式：",name[0])

#提取链接
movie_url = html_etree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/@href')
print ("这是数组形式：",movie_url)
print ("这是字符串形式：",movie_url[0])

#提取打分
rating = html_etree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[1]/@class')
print ("这是数组形式：",rating)
print ("这是字符串形式：",rating[0])

#提取本页所有电影名
li = html_etree.xpath('//*[@id="content"]/div/div[1]/ol/li')
for item in li:
    name = item.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
    print (name)

