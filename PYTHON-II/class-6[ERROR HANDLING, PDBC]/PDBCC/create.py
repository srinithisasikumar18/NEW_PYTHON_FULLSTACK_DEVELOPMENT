import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='#Srinithi4877',
                                  database='database1')
    cursor=dbcon.cursor()
    sql_St='''create table employees(
            eid int,
            ename varchar(32)
            );'''
    cursor.execute(sql_St)
    print("table is created")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()