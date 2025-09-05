n=[1,23,4,4,45,5,6]
#-----CREATE METHODS
m=n.copy()
print(m)
#-----READ METHODS
n.index(4)
print("index",n)
print("count",n.count(4))
n.append(7)
#----UPDATE METHODS
print("append",n)
n.insert(2,10)
print("insert",n)
n.extend([101,201,301,401])
print("extend",n)
n.sort()
print(n)
n.reverse()
print(n)
n.sort(reverse=True)
print(n)
#---DELETE METHODS
n.pop()
print(n)
n.remove(401)
print(n)
n.clear()
print(n)
print(n.pop())#---IndexError: pop from empty list
del n
print(n)#--------NameError