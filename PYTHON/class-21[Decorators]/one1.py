
def verify(func):
    def inner(name):
        if name=="Modi":
            print(name,"is a PM")
        else:
            return func(name)
    return inner