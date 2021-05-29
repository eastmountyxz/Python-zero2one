from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com/')
driver.save_screenshot('baidu.png')
