# read json file and write wmployees data into new json file
import json
fp1=open('data.json','r')
data=json.load(fp1)
fp2=open('emp.json','w')
emp=json.dump(data,fp2)
print("New file is created")