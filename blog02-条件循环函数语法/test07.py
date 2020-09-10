import webbrowser as web  
import time  
import os

i=0  
while i<5:  
    web.open_new_tab('http://www.baidu.com')  
    i=i+1  
    time.sleep(0.8)  
else:  
    os.system('taskkill /F /IM iexplore.exe')  
print('close IE')
