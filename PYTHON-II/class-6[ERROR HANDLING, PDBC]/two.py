# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# print(a/b)
# print("gm")




try:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    print(a/b)
except ValueError:
    print("Enter only intergers")
except ZeroDivisionError:
    print("Can't divide by zero")
# finally:
print("GM")