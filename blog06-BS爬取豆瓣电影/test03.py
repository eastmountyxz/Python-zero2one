# -*- coding: utf-8 -*-
# By:Eastmount CSDN
import urllib.request
import re 
from bs4 import BeautifulSoup
import codecs

#-----------------------------------爬取详细信息-------------------------------------
def getInfo(url, headers):
    page = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page)
    content = page.read()
    soup = BeautifulSoup(content, "html.parser")
    
    #电影简介
    print('电影简介:')
    info = soup.find(attrs={"id":"info"})
    print(info.get_text())
    other = soup.find(attrs={"class":"related-info"}).get_text()
    print(other.replace('\n','').replace(' ',''))
    
    #评论
    print('\n评论信息:')
    for tag in soup.find_all(attrs={"id":"hot-comments"}):
        for comment in tag.find_all(attrs={"class":"comment-item"}):
            com = comment.find("p").get_text()
            print(com.replace('\n','').replace(' ',''))
    print("\n\n\n----------------------------------------------------------------")
            
#-------------------------------------爬虫函数-------------------------------------
def crawl(url, headers):
    page = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser") 
    
    for tag in soup.find_all(attrs={"class":"item"}):
        #爬取序号
        num = tag.find('em').get_text()
        print(num)
        
        #电影名称
        name = tag.find_all(attrs={"class":"title"})
        zwname = name[0].get_text()
        print('[中文名称]', zwname)
        
        #网页链接
        url_movie = tag.find(attrs={"class":"hd"}).a
        urls = url_movie.attrs['href']
        print('[网页链接]', urls)
        
        #爬取评分和评论数
        info = tag.find(attrs={"class":"star"}).get_text()
        info = info.replace('\n',' ')
        info = info.lstrip()
        
        #正则表达式获取数字
        mode = re.compile(r'\d+\.?\d*')
        i = 0
        for n in mode.findall(info):
            if i==0:
                print('[电影分数]', n)
            elif i==1:
                print('[电影评论]', n)
            i = i + 1
        
        #获取评语
        getInfo(urls, headers)
        
#-------------------------------------主函数-------------------------------------
if __name__ == '__main__':
    #消息头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    #翻页
    i = 0
    while i<10:
        print('页码', (i+1))
        num = i*25 #每次显示25部 URL序号按25增加
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(url, headers)
        i = i + 1
        break
