from fastapi import APIRouter
router=APIRouter(prefix="/user")

'''
Usage : Create new User 
URL : http://127.0.0.1:8000/user/create 
Method Type:POST 
Required Fields: uname,email,gender,loc
Access Type:Public
'''
@router.post("/create")
def create_users():
    return {"msg":"new user created"}

'''
Usage : Fetch all users 
URL : http://127.0.0.1:8000/user/ 
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get('/')
def fetch_all_users():
    return {"msg":"fetch all users"}

'''
Usage : Fetch user by Id
URL : http://127.0.0.1:8000/user/101
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/{uid}")
def get_user(uid:int):
    return {"msg":"fetching user details",'uid':uid}

'''
Usage : update user by Id
URL : http://127.0.0.1:8000/user/update/101
Method Type:PUT
Required Fields: uname,email,gender,loc  
Access Type:Public
'''
@router.put('/update/{uid}')
def update_user(uid:int):
    return {"msg":"updating user by id","uid":uid}

'''
Usage : update user by Id
URL : http://127.0.0.1:8000/user/delete/101
Method Type:DELETE
Required Fields: uname,email,gender,loc  
Access Type:Public
'''
@router.delete('/delete/{uid}')
def delete_user(uid:int):
    return {"msg":"deleting user by id","uid":uid}