from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index_page():
    return {"message":"Application Root request"}

@app.post("/create")
def create_User():
    return {"message":"User Created Successfully"}

@app.get("/read")
def user_details():
    return {"message":"Fetching User Details"}

@app.put("/update")
def update_user():
    return {"message":"User Updated Successfully"}

@app.delete("/del")
def delete_User():
    return {"message":"User Deleted"}