import json
with open('employees.json','r') as fp:
    employees=json.load(fp)
    # print(employees)
male_count=0
female_count=0
for emp in employees:
    if emp['gender']=='Male':
        male_count+=1
    else:
        female_count+=1
print("no of male employees are:",male_count)
print("no of male employees are:",female_count)
# print("no of female employees are:",len(employees)-count)
print(fp.closed)