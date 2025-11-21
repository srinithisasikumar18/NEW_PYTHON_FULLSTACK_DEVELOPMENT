import fastapi 
from pydantic import BaseModel
app = fastapi.FastAPI()

data = [
        {"id":1,"user":"yagnesh"},
        {"id":2,"user":"yagnesh reddy"},
        {"id":3,"user":"reddy"},  
    ]

@app.get("/call/{id}")
def msg(id : int):
    li = [i for i in data if i["id"] == id ]
    if len(li) == 0:
        raise fastapi.HTTPException(status_code = 500,detail = "user db is empty")
    return {"states":"sucess","data":li}

@app.get("/alldata/")
def all():
    return {"data":data}


@app.put("/add/{id}/{user}")
def addData(id:int,user:str):
    data.append({"id":id,"user":user})
    return {"status":"sucessfuly insertses","data":data}

class me(BaseModel):
    id:int
    user:str = "yagnesh"
    
@app.post("/addpost")
def addDataviapost(datass : me):
    data.append({"id":datass.id,"user":datass.user})
    return {"status":"sucessfuly insertses","data":data}

@app.delete("/delete_user/{id}")
def delete_user(id:int):
    for i in data:
        if i["id"] == id:
            data.remove(i)
    return {"status":"deleted sucessfulty","data":data}