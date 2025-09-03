##TO CHECK GIVEN NUMBER IS 3-DIGIT NUMBER OR NOT
a=int(input("enter the first number"))
if a>=100 and a<=999:
    print("yes")
    # pass
else:
    print("no")



a=int(input("enter the first number"))
print(a>=100)
print(a<=999)
print(a>=100 and a<=999)