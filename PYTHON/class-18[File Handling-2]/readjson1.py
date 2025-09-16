#read emp.jsin and print the names of the user
import json
fp=open('emp.json','r')
employees=json.load(fp)
for emp in  employees:
    if emp['avail']==True:

        print(emp['ename'])