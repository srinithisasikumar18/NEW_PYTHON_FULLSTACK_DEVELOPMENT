import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['database2']
    coll_name=db['employees']
    total_users=coll_name.count_documents({})
    print(total_users)
    coll_name.delete_many({'gender':'Male'})
    print("deleted successfully")
    print(f'total female employees are {coll_name.count_documents({})}')
except:
    print("delete is not possible")
