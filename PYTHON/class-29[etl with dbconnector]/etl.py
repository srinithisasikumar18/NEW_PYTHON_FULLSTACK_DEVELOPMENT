import requests
import mysql.connector,json,csv
url=("https://dummyjson.com/users")
respone=requests.get(url)

sql_user=[]
data=respone.json()
users=data['users']
for user in users:
    sql_user.append((user['id'],
                     user['firstName'],
                     
                     user['email'],
                     user['gender']
    ))
try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='#Srinithi4877',database='onedb')
    cursor=dbcon.cursor()
    sql_st='''
    create table if not exists sql_users(
    user_id int,
    user_name varchar(32),
    user_email varchar(50),
    user_gender varchar(32)
    )
    '''
    sql_insert='''
    insert into sql_users(user_id,user_name,user_email,user_gender)
    values (%s,%s,%s,%s);

    '''
    dbcon.commit()
    cursor.execute(sql_st)
    cursor.executemany(sql_insert,sql_user)
    dbcon.commit()
except mysql.connector.Error as err:
        print(err)
# cursor.execute("select * from sql_users")
# rows=cursor.fetchall()
# print(rows)
finally:
    cursor.close()
    dbcon.close()