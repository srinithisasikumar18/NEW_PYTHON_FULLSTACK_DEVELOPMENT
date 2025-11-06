# read data.txt and write data into new filenwish.txt
fp1=open('data.txt','r')
fp2=open('wishes.txt','w')
data=fp1.read()
fp2.write(data)
print("new file is created")
fp1.close()
fp2.close()




