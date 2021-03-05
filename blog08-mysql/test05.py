# coding:utf-8
# By：Eastmount CSDN
import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',
                         port=3306, db='bookmanage', charset='utf8')
    cur=conn.cursor()
    
    #插入数据
    sql = '''insert into student values(%s, %s, %s)'''
    cur.execute(sql, ('3', 'xiaoyang', '男'))

    #查看数据
    print('\n插入数据:')
    cur.execute('select * from student')
    for data in cur.fetchall():
        print('%s %s %s' % data)
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
