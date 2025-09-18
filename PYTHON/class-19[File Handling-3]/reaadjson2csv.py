import json,csv
fp1=open('users.json','r')
fp2=open('users.csv','w',newline='')
users=json.load(fp1)
print(users)
new_user=[]
for user in users:
    new_user.append((user['u_id'],user['u_name'],user['gender']))
# print(new_user)

cw=csv.writer(fp2)
cw.writerow(["uid","uname","gender"])
cw.writerows(new_user)
print("new csv file cerated")