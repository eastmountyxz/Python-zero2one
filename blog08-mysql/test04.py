# coding:utf-8
# By：Eastmount CSDN
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',
                           port=3306, db='bookmanage', charset='utf8')
    cur = conn.cursor()
    sql = '''create table student(id int not null primary key auto_increment,
                                name char(30) not null,
                                sex char(20) not null
          )'''
    cur.execute(sql)
    
    #查看表
    print('插入后包含表:')
    cur.execute('show tables')
    for data in cur.fetchall():
        print('%s' % data)
    cur.close()
    conn.commit()
    conn.close()
    
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
