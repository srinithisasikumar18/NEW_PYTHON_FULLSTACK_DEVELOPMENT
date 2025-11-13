import mysql.connector,json,requests,csv,pymongo
from pymongo import MongoClient
response_data=requests.get('https://dummyjson.com/products')
data=response_data.json()
products=data['products']
print(type(data))
prod_data_tup=[]
prod_data_dict=[]

try:
    for product in products:
        prod_data_tup.append((product['id'],         #csv,sql
                            product['title'],
                            product['price'],
                            product['category'],
                            product['rating']))
        prod_data_dict.append({'pid':product['id'],        #json,mongodb
                            'ptitle':product['title'],
                            'pprice':product['price'],
                            'pcategory':product['category'],
                            'prating':product['rating']})
        # print(prod_data_dict)
        # print(prod_data_tup)

    # json
    fp1=open('product.json','w')
    json.dump(prod_data_dict,fp1)
    print("product.json file created")

    # csv
    fp2=open('products.csv','w',newline="")
    cw=csv.writer(fp2)
    cw.writerow(['pid','pname','pprice','pcategory','prating'])
    cw.writerows(prod_data_tup)
    print("csv file is created")

    # sql
    dbcon=None
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='#Srinithi4877',
                                  database='Products')
    cursor=dbcon.cursor()
    # sql_st='''create table if not exists Product(
    # p_id int,
    # p_title varchar(50),
    # p_price int,
    # p_category varchar(32),
    # p_rating float
    # )'''
    # cursor.execute(sql_st)
    print("databse and table is created")
    sql_st1='''insert into prod values(%s,%s,%s,%s,%s)'''
    cursor.executemany(sql_st1,prod_data_tup)
    dbcon.commit()
    print("data is inserted")

    # mongodb
    client=None
    client=MongoClient('mongodb://localhost:27017/')
    db=client['database2']
    coll_name=db['task']
    coll_name.insert_many(prod_data_dict)
    print("task has been created in MongoDB")

except mysql.connector.Error as err:
    print(err)
finally:
    fp1.close()
    fp2.close()
    dbcon.close()
    cursor.close()