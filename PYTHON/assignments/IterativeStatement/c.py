# 3. Program to calculate the sum of the first 10 natural numbers using for Loop- for
# loop and While loop?
num=1
sum=0
while num<=10:
    # print(num)
    num+=1
    sum=num+sum
    
print(sum)

sum=0
for i in range(1,11):
    print(i)
    sum=sum+i
print(sum)