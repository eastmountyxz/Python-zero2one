from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="F:\phantomjs-1.9.1-windows\phantomjs.exe")
driver.get("http://www.baidu.com")
data = driver.title
print(data)
