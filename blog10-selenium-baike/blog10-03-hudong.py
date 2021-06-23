# coding=utf-8  
#By：Eastmount CSDN 2021-06-23              
import os  
import codecs
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys       

driver = webdriver.Firefox()

#获取摘要信息
def getAbstract(name):  
    try:
        #新建文件夹及文件
        basePathDirectory = "Hudong_Coding"  
        if not os.path.exists(basePathDirectory):  
            os.makedirs(basePathDirectory)  
        baiduFile = os.path.join(basePathDirectory,"HudongSpider.txt")
        #文件不存在新建,存在则追加写入
        if not os.path.exists(baiduFile):  
            info = codecs.open(baiduFile,'w','utf-8')  
        else:  
            info = codecs.open(baiduFile,'a','utf-8')  

        url = "http://www.baike.com/wiki/" + name
        print(url)
        driver.get(url)  
        elem = driver.find_elements_by_xpath("//div[@class='summary']/div/span")
        content = ""
        for e in elem:
            content += e.text
        print(content)
        info.writelines(content+'\r\n')  
          
    except Exception as e: 
        print("Error: ",e)  
    finally:  
        print('\n') 
        info.write('\r\n')  
  
#主函数  
def main():
    languages = ["JavaScript", "Java", "Python", "Ruby", "PHP",
                 "C++", "CSS", "C#", "C", "GO"]
    print('开始爬取')
    for lg in languages:  
        print(lg)
        getAbstract(lg)  
    print('结束爬取')

if __name__ == '__main__':
    main()  
