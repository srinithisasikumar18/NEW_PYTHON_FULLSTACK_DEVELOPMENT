import csv,json
fp=open('json_data.json','r')
data=json.load(fp)
fp1=open('output.csv','w')
csv_write=csv.writer(fp1)
print("new file is created")
# csv_write.writerow(["eid", "ename"])
for item in data:
    csv_write.writerow([["eid"], ["ename"]])

fp1.close()