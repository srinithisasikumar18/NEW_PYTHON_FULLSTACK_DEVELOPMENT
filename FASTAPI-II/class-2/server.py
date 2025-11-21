from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def index_page():
    return {"msg":"Index Page"}
users=[]
class User(BaseModel):
    uid:int
    uname:str
    loc:str
@app.post("/create")
def create_user(user:User):
    users.append(user.dict())
    return {"msg":"user created successfully"}

@app.get("/read")
def read_user():
    return {"users":users}