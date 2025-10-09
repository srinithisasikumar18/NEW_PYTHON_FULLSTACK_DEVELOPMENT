import requests
import mysql.connector,json,csv
url=("https://dummyjson.com/users")
respone=requests.get(url)
sql_user=[]
employess=[]
data=respone.json()
users=data['users']
for user in users:
    sql_user.append((user['id'],
                     user['lastName'],
                     user['email'],
                     user['gender']))
    employess.append({'emp_id':user['id'],'emp_name':user['lastName'],'emp_email':user['email'],'emp_gender':user['gender']})
dbcon=mysql.connector.connect(host='localhost',user='root',password='#Srinithi4877',database='onedb')
cursor=dbcon.cursor()
sql_st='''
create table if not exists sql_users(
user_id int PRIMARY KEY ,
user_name varchar(32),
user_email varchar(50),
user_gender varchar(32)
)
'''
sql_insert='''
insert into sql_users(user_id,user_name,user_email,user_gender)
values (%s,%s,%s,%s);
'''
cursor.execute(sql_st)
cursor.executemany(sql_insert,sql_user)
dbcon.commit()
cursor.close()
dbcon.close()
fp=open('emp.json','w')
json.dump(employess,fp)
print("json file is created")