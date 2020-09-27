# -*- coding: utf-8 -*-
import csv
c = open("test-01.csv", "w", encoding="utf8", newline='')  #写文件
writer = csv.writer(c)
writer.writerow(['序号','姓名','年龄'])
 
tlist = []
tlist.append("1")
tlist.append("小明")
tlist.append("10")
writer.writerow(tlist)
print(tlist,type(tlist))
 
del tlist[:]  #清空
tlist.append("2")
tlist.append("小红")
tlist.append("9")
writer.writerow(tlist)
print(tlist,type(tlist))
 
c.close()
