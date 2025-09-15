fp1=open('abc.txt','r')
fp2=open('abc.txt','w')

print(fp1.readable())
print(fp1.writable())
print(fp1.name)
print(fp1.mode)
print(fp1.closed)

print(fp1.read())
data=fp1.readlines()
print(data)



