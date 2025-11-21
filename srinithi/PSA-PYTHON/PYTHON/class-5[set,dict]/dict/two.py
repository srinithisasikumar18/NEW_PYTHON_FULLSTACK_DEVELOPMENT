d={}
print(d)

emid={
    'eid':101,
    'ename':'kokila',
    'esalary':45000
}
print(emid)

###TO READ DICT WE USE THE KEYS
print(emid['eid'])
print(emid['ename'])
print(emid['esalary'])
# print(emid['loc'])   #------KeyError: 'loc'------------

####TO UPDATE THE DICT
emid['ename']='srinithi'
emid['ememail']='srinithi@gmail.com'
print(emid)

##DELETE
del emid['ememail']
print(emid)