# coding:utf-8
# By：Eastmount CSDN
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',
                           port=3306, db='bookmanage', charset='utf8')
    cur = conn.cursor()
    res = cur.execute('select * from books')
    print('表中包含', res, u'条数据\n')
    for data in cur.fetchall():
        print('%s %s %s %s' % data)
    cur.close()
    conn.close()
    
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
