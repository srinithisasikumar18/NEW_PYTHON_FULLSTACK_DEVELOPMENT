import requests,json
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
user=resp_data.json()
# print(type(user))
# users=list(user)
# print(users)
# print(type(user))
fp1=open('username_s.json','w')
for u_names in user:
    # print(type(u_names))
    user_name=u_names['name']
    print(user_name)
    json.dump(user_name,fp1,end="\n")
print("new file is created")
fp1.close()



# All the dict is printing

# import requests,json
# resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
# users=resp_data.json()
# fp1=open('users.json','w')
# json.dump(users,fp1)
# print("new file is created")
