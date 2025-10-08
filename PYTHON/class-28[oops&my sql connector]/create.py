import  mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                               user="root",
                               password="#Srinithi4877",
                               database='onedb'
                              )
print(dbcon)
cursor=dbcon.cursor()
print(type(cursor))
sql_st='''
        create table employees(
        eid int,
        ename varchar(32),
        esal float
        );
        '''
cursor.execute(sql_st)
dbcon.commit()
print("table created successfully")
cursor.close()
dbcon.close()