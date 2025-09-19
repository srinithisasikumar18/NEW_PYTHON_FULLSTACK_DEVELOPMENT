from two import login_req
def home_page(is_login):
    print("home page")
def products(is_login):
    print("product page")
@login_req
def orders(is_login):
    print("order page")
@login_req
def profile(is_login):
    print("profile page")
#--for both cases outputs are same
#---Case-1
# home_page(False)
# products(False)
# orders(False)                             home page
# profile(False)                            product page
#--Case-2                                   order page profile page
home_page(True)                            
products(False)
orders(False)
profile(False)                                           
                                           
