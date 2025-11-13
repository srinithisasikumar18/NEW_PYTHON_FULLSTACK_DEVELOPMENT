import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                user='root',
                                password='#Srinithi4877',
                                database='database1')
    cursor=dbcon.cursor()
    print(dbcon.is_connected(),"database connected successfully")
    # insert with the help of single statement 
    sql_st='''insert into users
    values
    (103,"priya","Female"),
    (104,"ramu","Male"),
    (105,"srinithi","Female")'''
    cursor.execute(sql_st)
    # insert with the help of executemany()
    sql_st1='''insert into users values (%s,%s,%s)'''
    values=[(105,"joshitha","Female"),(106,"kokila","female")]
    cursor.executemany(sql_st1,values)
    dbcon.commit()
    print("values inserted in to users table")
except mysql.connector.Error as err:
    print(err)
finally:
    dbcon.close()
    cursor.close()