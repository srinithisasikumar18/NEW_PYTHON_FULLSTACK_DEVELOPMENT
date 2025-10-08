import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='#Srinithi4877',
                              database='onedb')
cursor=dbcon.cursor()
cursor.execute("select * from employees")
employees=cursor.fetchall()
print(type(employees))
for emp in employees:
    print(emp)
print("Done")