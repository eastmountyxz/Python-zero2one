#-*- coding:utf-8 -*-
#By:Eastmount CSDN 2021-05-29
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()  
driver.get("https://www.baidu.com/")

print(driver.title)
print(driver.current_url)
# 百度一下，你就知道
# https://www.baidu.com/

news = driver.find_element_by_xpath("//div[@id='u1']/a[1]")
print(news.text)
print(news.get_attribute('href'))
print(news.location)
# 新闻
# http://news.baidu.com/
# {'y': 19.0, 'x': 456.0}
