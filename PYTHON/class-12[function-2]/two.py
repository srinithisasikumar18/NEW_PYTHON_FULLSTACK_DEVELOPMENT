def login():
    print("login success")
    return True,1,2,4.4,"kokila"
status=login()
print(status)



def login(name,password):
    # print(name,password)
    return name,password

status=login("srintihi","kokila")
print(status)