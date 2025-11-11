import csv
fp1=open('write_csv.csv','w',newline="")
cw=csv.writer(fp1)
cw.writerow(["eid","ename","esal"])
data=[
    (101,'rf',450000),
    (102,'sg',40000),
    (103,'pg',50000)
]
cw.writerows(data)
print("success")
fp1.close()