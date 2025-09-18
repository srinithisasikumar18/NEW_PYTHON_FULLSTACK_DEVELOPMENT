import csv
fp=open('emp.csv','r')
emp_data=csv.reader(fp)
employees=list(emp_data)
print(emp_data)
print(type(emp_data))
for emp in (employees)[1:]:
    print(emp[1])
# import csv
# fp=open('emp.csv','r')
# emp_data=csv.reader(fp)
# emp_data=list(dict(emp_data))
# print(emp_data)
# print(type(emp_data))
# # for emp in list(emp_data)[1:]:
#     print(emp[1])