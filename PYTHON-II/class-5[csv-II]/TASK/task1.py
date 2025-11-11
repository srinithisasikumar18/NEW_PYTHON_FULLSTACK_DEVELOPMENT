import requests,csv,json
fp1=open('emp.json','w',newline="")
fp2=open('u.csv','w')
response=requests.get('https://jsonplaceholder.typicode.com/users')
response_data=response.json()
# transform for json data
# data=json.load(response_data)
user_data_json=[]
for user in response_data:
     user_data_json.append({"uid":user['id'],
                           "uname":user['username'],
                           "email":user['email'],
                           "city":user['address']['city']})
json.dump(user_data_json,fp1)
print("new json file created")

# transform for csv file
cw=csv.writer(fp2)
user_data_csv=[]
cw.writerow(["uid","uname","email","city"])
for user in response_data:
    user_data_csv.append((user["id"],user["username"],user["email"],user["address"]["city"]))
    cw.writerows(user_data_csv)
print("success")








