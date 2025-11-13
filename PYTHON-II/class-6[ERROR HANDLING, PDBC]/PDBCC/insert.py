import mysql.connector
dbcon=None 
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='#Srinithi4877',
                                  database='database1')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='insert into employees values(101,"Rahul");'
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()