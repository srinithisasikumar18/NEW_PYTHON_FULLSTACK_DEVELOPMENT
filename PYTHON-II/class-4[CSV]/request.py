import requests
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
print(type(resp_data))
user=resp_data.json()
print(type(user))
print(resp_data.status_code)
for users in user:
    print(users['username'])
