from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get('/')
def home_page():
    return {"msg":"Application Root Request"}

'''
Usage:Create new user
API URL:http://127.0.0.1:8000/create 
Method Type:POST
Required Fields:uname,email,mobile
Access Type:Public
'''
@app.post('/create')
def create_user():
    return {"msg":"new user created"}

'''
Usage:fetch all users
API URL:http://127.0.0.1:8000/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get('/read')
def get_user():
    return {"msg":"Fetch all users"}

'''
Usage:update User by Uid
API URL:http://127.0.0.1:8000/update/101
Method Type:PUT
Required Fields:uname,email,mobile
Access Type:Public
'''
@app.put('/update/{uid}')
def update_user(uid:int):
    print(uid)
    return {"msg":"updating user","uid":uid}
'''
Usage:delete user by uid
API URL:http://127.0.0.1:8000/delete/101 
Method Type:DELETE
Required Fields:None
Access Type:Public
'''
@app.delete('/delete/{uild}')
def delete_user(uid:int):
    return {"msg":"User is deleted"}