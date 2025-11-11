import json,csv
fp1=open('users.json','r')
data=json.load(fp1)
# print(data)
fp2=open('users.csv','w',newline="")
cw=csv.writer(fp2)
cw.writerow(["id","name","email"])
users=[]
for user in data:
    users.append((user["id"],user["name"],user["email"]))
    cw.writerows(users)
print("users.csv created")
