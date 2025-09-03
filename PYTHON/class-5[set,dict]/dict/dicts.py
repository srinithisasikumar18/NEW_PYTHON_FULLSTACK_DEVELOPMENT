emp={
    'eid':101,
    'ename':"srinithi",
    "esal":45000,
    "email":"srinithi@gmail.com",
    "email":"srinithi@ibm.com"
}
print(emp)

print(emp['ename'])
print(emp['email'])
print(emp['loc'])#---KeyError

emp['eid']=103
emp['mother name']="kokila"
print(emp)

del emp['ename']
del emp
print(emp) #---NameError: name 'emp' is not defined
