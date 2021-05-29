#-*- coding:utf-8 -*-
#By:Eastmount 2021-05-29
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#启动驱动
driver = webdriver.Firefox()
driver.get("file://C:/Users/xiuzhang/Desktop/09.selenium/blog09.html")
print(driver.title)

#查找元素并输入内容
test_div = driver.find_elements_by_id('link')
for t in test_div:
    print(t.text)
