import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
print(resp.status_code)
products=product_data['products']
print(type(products))
print(len(products))
# print(products)
for product in products:
    print(product['title'])