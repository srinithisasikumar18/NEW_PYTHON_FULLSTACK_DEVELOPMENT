from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=[
    {"id":1,"name":"srinithi"},
    {"id":2,"name":"joshitha"},
    {"id":3,"name":"madhu"},
    {"id":4,"name":"kokila"},
    {"id":5,"name":"deepa"},
    {"id":6,"name":"subash"},
]
@app.get('/')
def index_page():
    return{"msg":"index created"}

class User(BaseModel):
    id:int
    name:str
@app.post('/create')
def create_user(New_user:User):
    data.append(New_user.dict())
    print("user created")
    return{"msg":"user created"}


@app.get('/read')
def get_user():
    return{"msg":"get user details","data":data}

@app.get("/read/{id}")
def get_user_by_id(id:int):
    for user in data:
        if user["id"]==id:
            return {"msg":"user found","user_id":user["id"],"user_name":user["name"]}
    return {"msg":"user is not in the list"}


@app.post('/update')
def update_user():
    return {"msg":"user details updated"}


@app.delete("/delete/{id}")
def delete_user(id:int):
    for u in data:
        if u["id"]==id:
            data.remove(u)
            return {"msg":"user deleted"}
    return {"msg":"user not found to delete"}