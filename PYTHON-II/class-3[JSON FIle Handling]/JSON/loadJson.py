import json
fp=open('data.json','r')
emp_data=json.load(fp)
print(emp_data)
for emp in emp_data:
    print(emp['ename'])