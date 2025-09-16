# here we importing json module bcoz whenever we want to convert the json data into python data we have use "load()" method
# read emp.json and printbemp name
import json
fp=open("emp.json","r")
employees=json.load(fp)#----we are converting into python data
print(employees)
print(type(employees))
for emp in employees:
    print(emp['ename'])