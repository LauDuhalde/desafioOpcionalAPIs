import requests
import json


url="https://reqres.in/api/users"
response = requests.get(url)
#1
users_data = response.json().get("data")

#2
new_user={
    "first_name": "Ignacio",
    "job":"Profesor"
}
users_data.append(new_user)
created_user=users_data.copy()
print(created_user)
print("--------------------------------------------\n")

#3 (no existe morpheus, así que actualicé a Emma)
for user in users_data:
    if user.get("first_name") == "Emma":
        user["residence"] = "zion"
        updated_user=users_data.copy()
        print(updated_user)
        print("--------------------------------------------\n")
        break
#4    
for user in users_data:
    if user["first_name"] == "Tracey":
        users_data.remove(user)
        print(users_data)
        print("--------------------------------------------\n")
        break

