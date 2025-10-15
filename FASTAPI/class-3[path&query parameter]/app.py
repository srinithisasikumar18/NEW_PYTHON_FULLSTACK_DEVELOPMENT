from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def home_page():
    return {"msg":"Home page"}
@app.get('/users')
def fetch_users():
    return {"msg":"Getting all users"}
@app.get('/users/{uid}')
def get_user(uid:int):
    print(uid)
    return {"msg":"User id","uid":uid}