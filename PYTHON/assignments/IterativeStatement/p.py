# 19. Program to print the reverse of digits of numbers.
num=int(input("enter the number"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+num
    print(rev)
    num=num//10