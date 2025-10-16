# CRUD on fastpi
# GET, POST, PUT, DELETE
from fastapi import FastAPI
app=FastAPI()
'''
usage:application root requets
api url: http://127.0.0.1:8000/
method type:get
required flieds:None
'''
@app.get('/')
def home_page():
    return {"msg":"Home page"}
'''
usage:displaying users
api url: http://127.0.0.1:8000/users
method type:get
required flieds:None
'''
@app.get('/users')
def fetch_users():
    return {"msg":"Getting all users"}
'''
usage:fetch users
api url: http://127.0.0.1:8000/users/uid
method type:get
required fields:None
'''
@app.get('/users/{uid}')
def get_user(uid:int):
    print(uid)
    return {"msg":"User id","uid":uid}
'''
usage:create new users
api url: http://127.0.0.1:8000/users/
method type:post
required fields:uid,uname,loc
'''
# @app.post('/users')
# # def create_users(user:User):
#     # pass