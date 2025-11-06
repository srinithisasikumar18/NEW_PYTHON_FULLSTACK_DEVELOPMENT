# syntax=open('file_name that has to be read', 'mode to which the is opened')
# default mode is read
# text file mode: r w a x(exclusive) r+(read and write) w+(write and read) a+(append+read) 
# binary file mode rb,wb,ab,xb, rb+,wb+,ab+
# methods: read(), readline(), readlines(), write()
fp=open('data.txt','r')
data=fp.read()
print(data)
fp.close()