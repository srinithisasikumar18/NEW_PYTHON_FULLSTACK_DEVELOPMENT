# writerows with csv 
import csv,json
fp1=open('users.csv','r')
fp2=open('users.json','w')
reader=csv.DictReader(fp1)
data=list(reader)
json.dump(data,fp2)
print("users.json new file is created")
