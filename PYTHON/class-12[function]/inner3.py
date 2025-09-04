# def user_module():

#     def login():
#         pass
#     def logout():
#         pass
    
# inner=user_module()
# print(inner)#---------returns None as a value
# print(type(inner))  



# def user_module():

#     def login():
#         pass
#     def logout():
#         pass
#     return 100
# inner=user_module()
# print(inner)#---------returns 100 as a value
# print(type(inner))


# def user_module():

#     def login():
#         print("login success")
#     def logout():
#         pass
#     return login
# inner=user_module()
# print(inner)#-------returns the address of the function
# print(type(inner))#---------returns login function as a value
# inner()


def user_module():
    def login():
        print("login success")
    def logout():
        print("logout")
    return login,logout  
inner1,inner=user_module()
inner()
inner1() #-------logout,login success

# def user_module():
#     def login():
#         print("login success")
#     def logout():
#         print("logout success")
#     return login, logout   # ✅ return both functions
# # unpack them
# login_func, logout_func = user_module()

# login_func()   # prints: login success
# logout_func()  # prints: logout success
