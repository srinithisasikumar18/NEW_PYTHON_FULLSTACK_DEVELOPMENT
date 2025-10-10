import requests
import pymongo
from pymongo import MongoClient
resp=requests.get("https://dummyjson.com/products")
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbcon']
products_col=db['beauty']
beauty=products_col.find()
for product in beauty:
    print(product['title'])