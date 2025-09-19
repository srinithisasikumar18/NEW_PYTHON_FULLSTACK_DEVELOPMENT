def verify(func): #---decortor function
    def inner(name):
        if name=="Modi":
            print(name,"is a PM")
        else:
            return func(name)
    return inner
@verify #--here we are calling the decorator
def wish(name):
    print("Hi",name,"Good Morining")
wish('srinithi')
wish('kokila')
wish('Modi')

# output
# Hi srinithi Good Morining
# Hi kokila Good Morining
# Modi is a PM