import requests,csv
response=requests.get('https://jsonplaceholder.typicode.com/users')
response_data=response.json()
# uid,username,email,city
fp1=open('users.csv','w',newline="")
cw=csv.writer(fp1)
cw.writerow(["uid","uname","email","city"])
for user in response_data:
    data=((user["id"], user["username"], user["email"], user["address"]["city"]))
    cw.writerow(data)
print("success")
# print(response_data)