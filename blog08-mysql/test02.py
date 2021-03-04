import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',
                         passwd='123456',port=3306)
    cur=conn.cursor()
    res = cur.execute('show databases')
    print(res)
    for data in cur.fetchall():
        print('%s' % data)
    cur.close()
    conn.close()
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
