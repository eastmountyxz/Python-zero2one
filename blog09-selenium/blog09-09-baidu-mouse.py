#-*- coding:utf-8 -*-
#By:Eastmount CSDN 2021-05-29
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#鼠标移动至图片上 右键保存图片
pic = driver.find_element_by_xpath("//div[@id='lg']/img")
action = ActionChains(driver).move_to_element(pic)
action.context_click(pic)

#选中图片右键鼠标，在弹出的对话框中点击光标向下按键
action.send_keys(Keys.ARROW_DOWN)

#将鼠标光标从弹出的对话框中移动至另存为选项，即为v值
action.send_keys('v') #另存为
action.perform()
