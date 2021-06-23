# coding=utf-8

"""
getinfo.py:获取信息
By：Eastmount CSDN 2021-06-23
"""
import os  
import codecs
import time
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys

#getInfobox函数: 获取国家5A级景区消息盒  
def getInfobox(name):  
    try:  
        #访问百度百科并自动搜索
        driver = webdriver.Firefox() 
        driver.get("http://baike.baidu.com/")  
        elem_inp = driver.find_element_by_xpath("//form[@id='searchForm']/input")  
        elem_inp.send_keys(name)  
        elem_inp.send_keys(Keys.RETURN)  
        time.sleep(1)
        print(driver.current_url)
        print(driver.title)
  
        #爬取消息盒InfoBox内容
        elem_name=driver.find_elements_by_xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dt")  
        elem_value=driver.find_elements_by_xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dd")
        """
        for e in elem_name:
            print(e.text)
        for e in elem_value:
            print(e.text)
        """

        #构建字段成对输出
        elem_dic = dict(zip(elem_name,elem_value)) 
        for key in elem_dic:  
            print(key.text,elem_dic[key].text)
        time.sleep(5)
        return
          
    except Exception as e: 
        print("Error: ",e)
    finally:  
        print('\n')
        driver.close()  
