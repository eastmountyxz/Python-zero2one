# coding:utf-8
# By:Eastmount
import requests
from lxml import etree

#设置浏览器代理,它是一个字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
num = 2
url = 'https://xxxx/list/' + str(num)

#向服务器发出请求
r = requests.get(url = url, headers = headers).text

#解析DOM树结构
count = 0
html_etree = etree.HTML(r)
div = html_etree.xpath('//*[@class="article-list"]/div')
for item in div:
    #标题
    value = item.xpath('./h4/a/text()')
    title = value[1].strip()
    count += 1
    print(title)
    #时间
    blog_time = item.xpath('./div/p/span[1]/text()')
    print(blog_time)

print("博客总数:", count)
