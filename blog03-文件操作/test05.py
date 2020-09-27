# -*- coding: utf-8 -*-
import csv
c = open("test-01.csv", "r", encoding="utf8")  #读文件
reader = csv.reader(c)
for line in reader:
    print(line[0],line[1],line[2])
c.close()
