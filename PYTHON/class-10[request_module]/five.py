import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['products']
no_of_beauty_products=0
for product in products:
    if product['category']=='beauty':
        print(product['title'])
        no_of_beauty_products+=1
print(no_of_beauty_products)