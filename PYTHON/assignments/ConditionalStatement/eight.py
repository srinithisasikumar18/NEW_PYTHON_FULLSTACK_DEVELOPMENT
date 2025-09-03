# 8. Write a program to find the biggest of given 3 numbers from the command
# prompt?
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>num2 and num1>num3:
    print("num1 is bigger")
elif num2>num3:
    print("num2 is bigger")
else:
    print("num3 is bigger")
