# -*- coding:utf-8 -*-
import urllib.request
   
# 函数功能：下载文件至本地，并显示进度
# a-已经下载的数据块, b-数据块的大小, c-远程文件的大小
def Download(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f' % per)
url = 'https://www.sina.com.cn'
local = 'd://sina.html'
urllib.request.urlretrieve(url, local, Download)
