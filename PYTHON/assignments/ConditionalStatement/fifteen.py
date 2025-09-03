# 15.Program to print given 3 numbers in descending order?
n=[]
num1=int(input("enter"))
num2=int(input("enter"))
num3=int(input("enter"))





# a=num1<num2 and num1<num3
# print(num1)
# b=num2<num1 and num2<num3
# print(num2)
# c=num3<num1 and num3<num2
# print(num3)
# print(n)


s=[]

n.append(num1)
n.append(num2)
n.append(num3)
print(n)
if num1<num2 and num1<num3:
    s.append(num1)
print(s)
# if num2<num1 and num2<num3:
#     s.append(num2)
#     print(s)
# if num1<num2 or num1<num3:
#     print(num1)
