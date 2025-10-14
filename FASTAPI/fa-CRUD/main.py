from fastapi import FastAPI
app=FastAPI()
'''
Usage:Application Root Request
API URL:http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public

'''
@app.get('/')
def home_page():
    return {"msg":"Application Root page"}

'''
Usage:Application About Page
API URL:http://127.0.0.1:8000/about
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get('/about')
def about_page():
    return {"msg":"about page"}

users=[
    {'uid':101,'uname':'Rahul','easl':4398.00},
    {'uid':102,'uname':'Priyanak','easl':54398.00},
    {'uid':103,'uname':'srinithi','easl':54398.00},
    {'uid':104,'uname':'kokila','easl':74398.00}
]
'''
Usage:Fetch All Users
API URL:http://127.0.0.1:8000/users
Method Type:GET
Required Fields: None
Access Type:Public

'''
@app.get('/users')
def users_page():
    return {"msg":"all users details"}
'''
Usage:Fetch user by Id
API URL:http://127.0.0.1:8000/users/101
Method Type:GET
Required Fields: None
Access:Type:Public
'''
@app.get('/users/{uid}')
def get_user(uid:int):
    print(type(uid))
    
    for user in users:
        if user['uid']==uid:
            return user    
        
    return {'msg':'user not exist'}

