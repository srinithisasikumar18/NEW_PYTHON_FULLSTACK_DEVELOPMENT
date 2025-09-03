def calc(a,b,c=100):
	print(a+b+c)
calc(1,2,3)#-------[6]
calc(1,2)#----------[103]---------TypeError: calc() missing 1 required positional argument: 'c'[if c=100 not provided]

calc(1,2)#----------if we give c=100 by default
