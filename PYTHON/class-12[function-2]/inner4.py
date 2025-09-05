def user_module(name,status):

    def login():
        print("login success")
    def logout():
        print("logout")
    if status==True:
        return login
    else:
        return logout
inner=user_module("srinithi",True)
inner()