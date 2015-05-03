import MySQLdb
from MySQLdb import *

def get_conn():
    host = "127.0.0.1"
    port =  3306
    logsdb= "dc"
    user = "root"
    password = "123456"
    con = MySQLdb.connect(host = host,  user = user,  passwd = password, db = logsdb, port =  port, charset = "utf8")
    return con

def close(con):
    con.close()

def get_cursor(con):
    return con.cursor()

if __name__ == '__main__':
    con = get_conn()
    print con
    cursor = get_cursor(con)
    ret = cursor.execute("select * from money")
    print ret
    results = cursor.fetchall()
    print results
    for item in results:
        print item[0], item[1]
    try:
        cursor.execute("update money set amt=amt-6 where name='Eve' ")
        cursor.execute("update money set amt=amt+6 where name='Ida' ")
        cursor.close()
        con.commit()
    except MySQLdb.Error, e:
        print "Transcation failed, rollig back, Error was: "
        print e.args
        try:
            conn.rollback()
        except:
            pass
               
    close(con)
