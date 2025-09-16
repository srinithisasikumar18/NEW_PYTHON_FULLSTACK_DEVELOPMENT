import json
fp1=open('users.json','r')
fp2=open('males.json','w')
users=json.load(fp1)
male_users=[]
for male_user in users:
    if male_user['gender']=='Male':
        male_users.append(male_user)
json.dump(male_users,fp2)
print(len(male_users))
fp1.close()
fp2.close()