import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                              user="root",
                              password="#Srinithi4877",
                              database="onedb"
                              )
print(dbcon)
# creating to cursor so that python understand the sql cmds
cursor=dbcon.cursor()
print(type(cursor))
sql_st='''
create table if not exists orders(
    oid int,
    oname varchar(32),
    odetails varchar(32)
)
'''
cursor.execute(sql_st)
print("table creates successfully")
sql_insert='''
INSERT INTO ORDERS (oid,oname,odetails)
VALUES
(%s,%s,%s)
'''
values=[
(101,'Mp1','Pen'),
(102,'Mp2','Pen'),
(103,'Mp3','Pen')
]

cursor.executemany(sql_insert,values)
dbcon.commit()
print("Values inserted successfully")

cursor.close()
dbcon.close()
