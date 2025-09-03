def sum(a,b):
	print("a value",a,"---b value",b)
sum(1,2)
sum(1,2,3)#---TypeError: sum() takes 2 positional arguments but 3 were given



def sum(a,*b):
    print("a value",a,"---b value",b)
sum(1,2)
sum(1,2,3)
sum(1,2,3,4)
sum(1,2,3,4,5)