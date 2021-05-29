#-*- coding:utf-8 -*-
#By:Eastmount CSDN 2021-05-29
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()  
driver.get("https://www.baidu.com/")
elem = driver.find_element_by_id("kw")
elem.send_keys("Eastmount") #Python
elem.send_keys(Keys.RETURN)
