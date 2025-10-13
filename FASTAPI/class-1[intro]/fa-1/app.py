from fastapi import FastAPI
app=FastAPI()
'''
Usage:Home page
API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public

'''
@app.get('/')
def home_page():
    return {"msg":"Home Page"}
'''
Usage:Home page
API URL: http://127.0.0.1:8000/about
Method Type:GET
Required Fields: None
Access Type:Public

'''
@app.get('/about')
def about_page():
    return {"msg":"About Page"}
'''
Usage:Home page
API URL: http://127.0.0.1:8000/contact
Method Type:GET
Required Fields: None
Access Type:Public

'''
@app.get('/contact')
def about_contact():
    return {"msg":"Contact Page"}