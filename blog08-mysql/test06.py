#-*- coding:utf-8 -*-
# By：Eastmount CSDN
import sqlite3

#连接数据库：如果数据库不存在则创建
conn = sqlite3.connect('test6.db')
cur = conn.cursor()
print('数据库创建成功.\n')

#创建表 PEOPLE(编号,姓名,年龄,公司,薪水)
cur.execute('''CREATE TABLE PEOPLE
               (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL,
                COMPANY        CHAR(50),
                SALARY         REAL);
          ''')
print("PEOPLE表创建成功.\n")
conn.commit()

#插入数据
cur.execute("INSERT INTO PEOPLE (ID,NAME,AGE,COMPANY,SALARY) \
      VALUES (1, '小杨', 26, '华为', 10000.00 )");
cur.execute("INSERT INTO PEOPLE (ID,NAME,AGE,COMPANY,SALARY) \
      VALUES (2, '小颜', 26, '百度', 8800.00 )");
cur.execute("INSERT INTO PEOPLE (ID,NAME,AGE,COMPANY,SALARY) \
      VALUES (3, '小红', 28, '腾讯', 9800.00 )");
conn.commit()
print("数据插入成功.\n")

#查询操作
cursor = cur.execute("SELECT id, name, age, company, salary  from PEOPLE")
print("数据查询成功.")
print("序号", "姓名", "年龄", "公司", "薪水")
for row in cursor:
    print(row[0], row[1], row[2], row[3], row[4])
print('')

#更新操作
cur.execute("UPDATE PEOPLE set COMPANY = '华为' where ID=2")
conn.commit()
print("数据更新成功.")
cursor = cur.execute("SELECT id, name, company from PEOPLE")
for row in cursor:
    print(row[0], row[1], row[2])
print('')

#删除操作
cur.execute("DELETE from PEOPLE where COMPANY='华为';")
conn.commit()
print("数据删除成功.")
cursor = cur.execute("SELECT id, name, company from PEOPLE")
for row in cursor:
    print(row[0], row[1], row[2])
print('')

#关闭连接
conn.close()
