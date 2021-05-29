#-*- coding:utf-8 -*-
#By:Eastmount CSDN 2021-05-29
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains

#打开浏览器
driver = webdriver.Firefox()  
driver.get("https://www.baidu.com/")
time.sleep(1)

#点击登录链接
logins = driver.find_elements_by_name("tj_login")
for login in logins:
    print(login.text)
    print(login.get_attribute('href'))
    if login.is_displayed():
        login.click()
time.sleep(1)

#通过二次定位寻找用户名登录按钮
uesrlogins = driver.find_elements_by_xpath("//div[@class='tang-pass-footerBar']/p")
for uesrlogin in uesrlogins:
    print(uesrlogin.text)
    if uesrlogin.is_displayed():
        uesrlogin.click()

#输入密码并登陆
name = driver.find_element_by_name("userName")
name.clear
name.send_keys("Eastmount")     

pwd = driver.find_element_by_name("password")
pwd.clear
pwd.send_keys("12345678")

#暂停输入验证码 按回车键登录
time.sleep(5)
pwd.send_keys(Keys.RETURN)
driver.close()         
