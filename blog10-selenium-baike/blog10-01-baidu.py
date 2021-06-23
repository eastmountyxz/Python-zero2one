# -*- coding: utf-8 -*-
"""
test10_01_baidu.py
    定义了主函数main并调用getinfo.py文件
By：Eastmount CSDN 2021-06-23
"""
import codecs   
import getinfo  #引用模块

#主函数 
def main():
    #文件读取景点信息 
    source = open('data.txt','r',encoding='utf-8') 
    for name in source:  
        print(name)
        getinfo.getInfobox(name)
    print('End Read Files!') 
    source.close()
if __name__ == '__main__':
    main()
