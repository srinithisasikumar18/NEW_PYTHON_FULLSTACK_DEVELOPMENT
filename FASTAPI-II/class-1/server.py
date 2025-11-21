from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def index_page():
    return {"msg":"index page"}

@app.get("/about")
def about():
    return {"msg":"about page"}

@app.get("/contact")
def contact():
    return {"msg":"contact page"}