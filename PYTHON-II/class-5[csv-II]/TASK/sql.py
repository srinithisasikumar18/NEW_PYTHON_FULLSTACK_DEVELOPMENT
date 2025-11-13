import mysql.connector,requests
response=requests.get('https://jsonplaceholder.typicode.com/users')
response_data=response.json()
dbcon=None
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877',
                              database='taskdb')
print("database created")

cursor=dbcon.cursor()
sql_st='''create table if not exists users(
uid int,
uname varchar(32),
uemail varchar(32),
ucity varchar(32)
)'''
cursor.execute(sql_st)
print("table users created")
sql_st1=''' insert into users values
(%s,%s,%s,%s)'''
for user in response_data:
    user_id=user['id']
    user_name=user['name']
    user_email=user['email']
    user_city=user['address']['city']
    cursor.execute(sql_st1,(user_id,user_name,user_email,user_city))
dbcon.commit()
print("data inserted")