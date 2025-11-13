import json,mysql.connector,requests,csv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,PyMongoError
try:
    respone_data=requests.get('https://jsonplaceholder.typicode.com/users')
    data=respone_data.json()
    user_data_t=[]
    user_data_d=[]
    for user in data:
        user_data_t.append((user['id'],
                            user['name'],
                            user['email'],
                            user['address']['city']))
        user_data_d.append({'uid':user['id'],
                            'unmae':user['name'],
                            'uemail':user['email'],
                            'city':user['address']['city']})
    # JSON
    fp1=open('user.json','w')
    json.dump(user_data_d,fp1)
    # csv
    fp2=open('users.csv','w',newline="")
    cw=csv.writer(fp2)
    cw.writerow(["id","name","email","city"])
    cw.writerows(user_data_t) 
    # sql
    dbcon=None
    cursor=None
    dbcon=mysql.connector.connect(host='localhost',
                                      user='root',
                                      password='#Srinithi4877',
                                      database='database1')
     # print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''create table if not exists taskss (
            uid int,
            uname varchar(32),
            uemail varchar(32),
            ucity varchar(32)
            )'''
        
    sql_st1='''insert into taskss(uid,uname,uemail,ucity) values (%s,%s,%s,%s)'''
    cursor.execute(sql_st)
    cursor.executemany(sql_st1,user_data_t)
    dbcon.commit()


    # mongoDB
    client=None
    client=MongoClient('mongodb://localhost:27017/')
    db=client['database2']
    coll_name=db['task2']
    coll_name.insert_many(user_data_d)
    print("task2 is created in mongoDB") 
    print("table is created")
    print("json data is loaded into users.json")
    print("csv data is loaded into users.csv")
    print("sql data is loaded")  
except PyMongoError as err  :
    print(err)
except ConnectionFailure as connection:
    print(connection)
finally:
    fp1.close()
    fp2.close()
    cursor.close()
    dbcon.close()
