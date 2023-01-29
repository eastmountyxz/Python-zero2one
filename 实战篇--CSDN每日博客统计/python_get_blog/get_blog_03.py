# coding:utf-8
# By:Eastmount
import requests
from lxml import etree

#--------------------------------------------------------------------------
#采集CSDN博客数据
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

num = 1
count = 0
title_list = []
time_list = []
year_list = []
while num<=18:
    url = 'https://xxx/list/' + str(num)

    #向服务器发出请求
    r = requests.get(url = url, headers = headers).text

    #解析DOM树结构
    html_etree = etree.HTML(r)
    div = html_etree.xpath('//*[@class="article-list"]/div')
    for item in div:
        #标题
        value = item.xpath('./h4/a/text()')
        title = value[1].strip()
        count += 1
        #print(title)
        title_list.append(title)
        
        #日期和时间
        data = item.xpath('./div/p/span[1]/text()')
        data = str(data[0])

        #提取日期
        year = data.split("-")[0]
        month = data.split("-")[1]
        day = data.split("-")[2].split(" ")[0]
        blog_time = str(year) + "-" + month + "-" + day
        #print(blog_time, year)
        time_list.append(blog_time)
        year_list.append(year)
    num += 1
print("博客总数:", count)
print(len(title_list), len(time_list), len(year_list))

#--------------------------------------------------------------------------
#生成一年所有日期
import arrow
 
#判断闰年并获取一年的总天数
def isLeapYear(years):
    #断言：年份不为整数时抛出异常
    assert isinstance(years, int), "请输入整数年，如 2018"
    #判断是否是闰年
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  
        days_sum = 366
        return days_sum
    else:
        days_sum = 365
        return days_sum
 
#获取一年的所有日期
def getAllDayPerYear(years):
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    return all_date_list

all_date_list = getAllDayPerYear("2013")
print(all_date_list)

#--------------------------------------------------------------------------
#遍历一年所有日期发表博客的数量
k = 0
res = {}
while k<len(all_date_list):
    tt = all_date_list[k]
    res[tt] = 0
    m = 0
    while m<len(time_list):
        tt_lin = time_list[m]
        if tt==tt_lin:
            res[tt] += 1
        m += 1
    k += 1
print("\n------------------------统计结束-------------------------\n")
print(res)
#统计发表博客数
count_blog = 0
for i in res.keys():
    if res[i] > 0:
        count_blog += res[i]
print(count_blog)

#--------------------------------------------------------------------------
#存储至Json文件
import json
print(type(res), len(res))
with open("data-2013.json", "w", encoding='utf-8') as f:
    json.dump(res, f)
    print("文件写入....")
