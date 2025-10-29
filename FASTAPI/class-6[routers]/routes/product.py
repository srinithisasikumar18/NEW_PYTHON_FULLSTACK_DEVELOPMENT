from fastapi import APIRouter
router=APIRouter(prefix="/product")

'''
Usage : update product by Id
URL : http://127.0.0.1:8000/product/update/10
Method Type:PUT
Required Fields: pname,qty,price  
Access Type:Public
'''
@router.put("/update/{pid}")
def update_product(pid:int):
    return {"msg":"product updated","pid":pid}

'''
Usage : Delete product by Id
URL : http://127.0.0.1:8000/product/delete/101
Method Type:DELETE
Required Fields: None
Access Type:Public
'''
@router.delete("/delete/{pid}")
def delete_product(pid:int):
    return {"msg":"product deleted","pid":pid}