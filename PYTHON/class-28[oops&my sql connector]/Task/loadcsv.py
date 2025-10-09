import requests
import mysql.connector,json,csv
url=("https://dummyjson.com/users")
respone=requests.get(url)
sql_user=[]
# employess=[]
data=respone.json()
users=data['users']
for user in users:
    sql_user.append((user['id'],
                     user['lastName'],
                     user['email'],
                     user['gender']))
    # employess.append({user})
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
print("table with data is created")
fp=open('users.csv','w',newline='')
cw=csv.writer(fp)
cw.writerow(["user_id","user_name","user_emnail","user_gender"])
cw.writerows(sql_user)
print("data inserted into csv file")
