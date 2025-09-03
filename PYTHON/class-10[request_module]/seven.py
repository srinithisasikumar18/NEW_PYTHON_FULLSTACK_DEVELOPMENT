import requests
res=requests.get("https://jsonplaceholder.typicode.com/users")
print(res) #----- it will print the response_status of the request
print(res.text)#---------it will print the object in the request[the default format is string]
i=res.json()#-------this will give you the objects in list and dict format
for iss in i:
    print(iss['username'], "|", iss["id"])