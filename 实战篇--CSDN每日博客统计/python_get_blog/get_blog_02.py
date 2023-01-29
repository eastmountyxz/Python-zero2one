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
url = 'https://xxx/list/' + str(num)

#向服务器发出请求
r = requests.get(url = url, headers = headers).text

#解析DOM树结构
count = 0
title_list = []
time_list = []
year_list = []
html_etree = etree.HTML(r)
div = html_etree.xpath('//*[@class="article-list"]/div')
for item in div:
    #标题
    value = item.xpath('./h4/a/text()')
    title = value[1].strip()
    count += 1
    print(title)
    title_list.append(title)
    
    #日期和时间
    data = item.xpath('./div/p/span[1]/text()')
    data = str(data[0])
    #print(data)

    #提取日期
    year = data.split("-")[0]
    month = data.split("-")[1]
    day = data.split("-")[2].split(" ")[0]
    blog_time = str(year) + "-" + month + "-" + day
    print(blog_time, year)
    time_list.append(blog_time)
    year_list.append(year)
print("博客总数:", count)
