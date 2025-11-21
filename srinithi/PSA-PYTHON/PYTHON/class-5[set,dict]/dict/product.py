product={
    'pid':101,
    'pname':'mpen',
    'price':30,
    'details':{
        'color':['black','orange','blue'],
        'size':'small'
    }
}


print(product)
print(product['pid'])
print(product['details'])
print(product['details']['size'])
print(product['details']['color'][2]) 

###DELETE 
# del product['pid']
# del product
# print(product)