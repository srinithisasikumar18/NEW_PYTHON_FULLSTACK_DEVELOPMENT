import json,csv
fp1=open('emp.json','r')
fp2=open('males.csv','w',newline='')
employees=json.load(fp1)
male_users=[]
for males in employees:
    if males['gender']=='Male':
        male_users.append((males['u_id'],males['u_name'],males['gender']))
cw=csv.writer(fp2)
cw.writerow(["uid","uname","gender"])
cw.writerows(male_users)