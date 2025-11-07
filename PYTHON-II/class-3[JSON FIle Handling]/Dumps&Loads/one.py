# loads---json===>python
import json
emp_str='''{"eid":101,"ename":"srinithi","avail":true},
{"eid":102,"ename":"deepa","avail":true},
{"eid":103,"ename":"karthik","avail":true},
{"eid":103,"ename":"subash","avail":true},
'''
# print(emp_str)
# print(type(emp_str))
# {"eid":101,"ename":"srinithi","avail":true},
# {"eid":102,"ename":"deepa","avail":true},
# {"eid":103,"ename":"karthik","avail":true},
# {"eid":103,"ename":"subash","avail":true},
# <class 'str'>

employees=json.loads(emp_str)
print(employees)
print(type(employees))