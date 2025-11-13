import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877',
                              database='database1')
cursor=dbcon.cursor()
# CRUD
# CREATE
sql_st='''create table if not exists users(
uid int,
uname varchar(32),
ugender varchar(32));'''
sql_st1='''insert into users values(%s,%s,%s)'''
values=(101,"rahul","Male"),(102,"modi","Male")
cursor.execute(sql_st)
print("Table created")
cursor.executemany(sql_st1,values)
print("Values also inserted")
dbcon.commit()
print("Table is created")
dbcon.close()
cursor.close()