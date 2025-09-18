import json,csv
fp1=open('emp.json','r')
fp2=open('female.csv','w',newline='')
employees=json.load(fp1)
female_users=[]
for female in employees:
    if female['gender']=='Female':
        female_users.append((female['u_id'],female['u_name'],female['gender']))
s=csv.writer(fp2)
s.writerow(['uid','uname','gender'])
s.writerows(female_users)
print("new csv file created")