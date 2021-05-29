#-*- coding:utf-8 -*-
#By:Eastmount 2021-05-29
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#启动驱动
driver = webdriver.Firefox()
driver.get("file://C:/Users/xiuzhang/Desktop/09.selenium/blog09_02.html")
print(driver.title)

#分别定位三个超链接
test_poet1 = driver.find_element_by_link_text('Dufu')
print(test_poet1.text)
test_poet2 = driver.find_element_by_link_text('LiShangYing')
print(test_poet2.text)
test_poet3 = driver.find_element_by_link_text('DuMu')
print(test_poet3.text)

#定位超链接部分元素
test_poet4 = driver.find_element_by_partial_link_text('Du')
print(test_poet4.text)

#定位超链接部分元素且定位多个元素
test_poet5 = driver.find_elements_by_partial_link_text('Du')
for t in test_poet5:
    print(t.text)
