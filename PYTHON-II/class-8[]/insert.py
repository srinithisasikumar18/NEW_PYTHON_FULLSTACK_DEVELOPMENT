import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['database2']
    user_col=db['users']
    user_col.insert_one({"uid":101,"uname":"rahul"})
    print("usesrs has been created")
except pymongo.errors as err:
    print(err)