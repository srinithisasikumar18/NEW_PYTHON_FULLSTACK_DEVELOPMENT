fp=None
fp=open('abc.txt','r')
data=fp.read()
print(data)
fp.close()
#FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'