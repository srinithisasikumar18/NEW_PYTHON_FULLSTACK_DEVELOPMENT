# here we are converting json str into pyhton
import json
employees_str='''[
    {"eid":101,"ename":"rahul","avail":true},
    {"eid":102,"ename":"srinithi","avail":false},
    {"eid":103,"ename":"kokila","avail":true},
    {"eid":104,"ename":"madhu","avail":false}
]
'''
employees=json.loads(employees_str)
print(employees)