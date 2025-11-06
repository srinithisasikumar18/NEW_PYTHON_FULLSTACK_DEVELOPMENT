# how invoke inner function----with the help of inner function reference
def outer():
    print("outer function")
    def inner():
        print("inner function")
    return 100,200
s=outer()
print(s)


def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner
s=outer()
s()



def calc():
    def add():
        print("addition")
    # return add
    def muitliply():
        print("multiplication")
    return add,muitliply

    # return add
a,mul=calc()
a()
mul()

values=calc()
values[0]()