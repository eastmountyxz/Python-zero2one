# -*- coding:utf-8 -*-
# By:Eastmount CSDN
import urllib.request
import re 
from bs4 import BeautifulSoup

# 爬虫函数
def crawl(url, headers):
    page = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page)
    contents = page.read()
    #print(contents)
    
    soup = BeautifulSoup(contents, "html.parser")
    print('豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数')
    for tag in soup.find_all(attrs={"class":"item"}):
        content = tag.get_text()
        content = content.replace('\n','')   #删除多余换行
        #print(content, '\n')

    for tag in soup.find_all(attrs={"class":"item"}): 
        title = tag.find_all(attrs={"class":"title"})           #电影名称
        info = tag.find(attrs={"class":"star"}).get_text()      #爬取评分和评论数
        print(title[0])
        print(info.replace('\n',''))

# 主函数
if __name__ == '__main__':
    url = 'http://movie.douban.com/top250?format=text'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    crawl(url, headers)
