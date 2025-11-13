import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['database2']
    user_col=db['employees']
    user_data=user_col.find()
    employee=list(user_data)
    for emp in employee:
        print(emp['name'])
except :
    pass