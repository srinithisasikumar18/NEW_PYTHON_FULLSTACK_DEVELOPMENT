import requests,pymongo
from pymongo import MongoClient
resp=requests.get('https://dummyjson.com/products')
data=resp.json()
ratings=[]
rating_data=data['products']