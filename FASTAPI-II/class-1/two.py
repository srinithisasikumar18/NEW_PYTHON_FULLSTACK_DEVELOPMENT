from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=[
    {"id":1,"name":"srinithi"},
    {"id":2,"name":"joshitha"},
    {"id":3,"name":"deepa"},
    {"id":4,"name":"karthik"},
    {"id":5,"name":"subashh"},
]

@app.get("/")
def get_user():
    return {"status":"success","users":data}

@app.get("/id/{id}")
def get_user_by_id(id:int):
    for i in data:
        if i["id"]==id:
            return {"user":i}
    return {"msg":"user not found"}

class User(BaseModel):
    id:int
    name:str
@app.put("/addUser")
def update_user(user: User):
    data.append({"id":user.id,"user":user.name})
    return {"user":data}

