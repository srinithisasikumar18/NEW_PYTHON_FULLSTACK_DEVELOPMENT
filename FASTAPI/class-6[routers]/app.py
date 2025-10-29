from fastapi import FastAPI
from routes.user import router as userrouter
from routes.product import router as prodrouter
# create fastapi app
app=FastAPI()
# create root request
@app.get("/")
def index_page():
    return {"msg":"Application Root Request"}

app.include_router(userrouter)
app.include_router(prodrouter)