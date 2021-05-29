#-*- coding:utf-8 -*-
#By:Eastmount 2021-05-29
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#启动驱动
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
assert "百度" in driver.title
print(driver.title)

#查找元素并输入内容
elem = driver.find_element_by_name("wd")
elem.send_keys("数据分析")
elem.send_keys(Keys.RETURN)

#截图并退出
time.sleep(10)
driver.save_screenshot('baidu.png')
driver.close()
driver.quit()
