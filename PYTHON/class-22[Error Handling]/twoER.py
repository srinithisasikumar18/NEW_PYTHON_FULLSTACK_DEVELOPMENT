# try with multiple except blocks
try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ValueError as Ve:
    print(Ve)
except ZeroDivisionError as Zde:
    print(Zde)

print("good morning")



try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except (ValueError,TypeError,ZeroDivisionError) as err:
    print(err)
print("good morning")