# -*- coding:utf-8 -*-
import urllib.request

url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
local = 'baidu.png'
urllib.request.urlretrieve(url, local)
