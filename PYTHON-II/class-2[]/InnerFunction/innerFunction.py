# function--Inner function
def calc():
    print("calculation")
    def add():
        print("addition")
    add()
    add()
    def muiltiplication():
        print("muiltiplication")
    muiltiplication()
    muiltiplication()
    muiltiplication()
calc()