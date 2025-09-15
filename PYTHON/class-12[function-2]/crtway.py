# first way
def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return True
x=user_module()
print(x)


# SEcond way
def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return login() #---here we are using login() to be printed which returns None
x=user_module()
print(x) #----None

# third way
def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return login()
x=user_module
print(x)

# fourth way
def user_module():
    def login():
        print("login success")
    def logout():
        print("logout success")
    return login #--login function reference
x=user_module()
x()