# coding=utf-8
#By：Eastmount CSDN 2021-06-23
import time            
import re            
import os     
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        

driver = webdriver.Firefox() 
driver.get("https://en.wikipedia.org/wiki/Category:G20_nations")  
elem = driver.find_elements_by_xpath("//div[@class='mw-category-group']/ul/li/a")
name = []    #国家名
urls = []    #国家超链接

#爬取链接
for e in elem:
    print(e.text)
    print(e.get_attribute("href"))
    name.append(e.text)
    urls.append(e.get_attribute("href"))
print(name)
print(urls)

#爬取内容
for url in urls:
    driver.get(url)  
    elem = driver.find_element_by_xpath("//div[@class='mw-parser-output']/p[1]").text  
    print(elem)
