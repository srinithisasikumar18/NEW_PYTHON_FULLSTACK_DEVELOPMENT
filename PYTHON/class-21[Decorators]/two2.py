def smart_div(func):
    def inner(a,b):
        if b==0:
            print("can't divide by zero")
        else:
            return func(a,b)
    return inner

    
