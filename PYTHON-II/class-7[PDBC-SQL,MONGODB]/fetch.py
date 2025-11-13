import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                user='root',
                                password='#Srinithi4877',
                                database='database1')
    cursor=dbcon.cursor()
    print(dbcon.is_connected(),"database connected successfully")
    sql_st='''Select * from users'''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    print(employees)
    for emp in employees:
        print(emp[1])
except mysql.connector.Error as err:
    print(err)
finally:
    dbcon.close()
    cursor.close()