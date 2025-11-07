import json
emp_str='''[
    {"eid":101,"ename":"Srinithi"},
    {"eid":102,"ename":"kokila"},
    {"eid":103,"ename":"karthik"}
]'''
employees=json.loads(emp_str)
data=json.dumps(employees)
# print("New file is created",data)
print(type(data))
