import requests
import pymongo
from pymongo import MongoClient
resp=requests.get("https://dummyjson.com/products")
product_data=resp.json()
products=product_data['products']
# print(len(products))
# print(type(products))
#Transform
# ----without filter
beauty_products=[]
for product in products:
    if product['category']=='beauty':
        beauty_products.append(product)
#Load
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbcon']
products_col=db['beauty']
products_col.insert_many(beauty_products)
print("beauty product inserted successfully")