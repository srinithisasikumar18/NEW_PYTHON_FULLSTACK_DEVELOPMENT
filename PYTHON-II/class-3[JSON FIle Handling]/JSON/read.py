# read data.json and read all employees and orint available employees
import json
fp=open('data.json','r')
employees=json.load(fp)
for emp in employees:
    if emp['avail']==True:
        print(emp['ename'])
fp.close()