import mysql.connector,json,requests,csv
response_data=requests.get('https://dummyjson.com/products')
data=list(response_data.json())
print(type(data))
prod_data_tup=[]
prod_data_dict=[]
for product in data:
    prod_data_tup.append((product['id'],
                         product['title'],
                         product['price'],
                         product['category'],
                         product['rating']))
    prod_data_dict.append({'pid':product['id'],
                          'ptitle':product['title'],
                          'pprice':product['price'],
                          'pcategory':product['category'],
                          'prating':product['rating']})
# json
fp1=open('product.json','w')
json.dump(prod_data_dict,fp1)
print("product.json file created")