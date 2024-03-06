import requests
import json


url="https://reqres.in/api/users"
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:
    print("La solicitud GET fue exitosa")
    #1
    users_data = response.json().get("data")

    #2
    new_user={
        "first_name": "Ignacio",
        "job":"Profesor"
    }
    
    created_user=users_data.copy()
    created_user.append(new_user)
    print(created_user)
    print("--------------------------------------------\n")

    #3 (no existe morpheus, así que actualicé a Emma)
    updated_user=users_data.copy()
    for user in updated_user:
        if user.get("first_name") == "Emma":
            user["residence"] = "zion"
            break
    print(updated_user)
    print("--------------------------------------------\n")
    
    #4    
    remove_user=users_data.copy()
    for user in remove_user:
        if user["first_name"] == "Tracey":
            remove_user.remove(user)
            break
    print(remove_user)
    print("--------------------------------------------\n")
    
elif response.status_code == 404:
    print("La solicitud GET falló: recurso no encontrado")
else:
    print(f"La solicitud GET falló con el código de estado {response.status_code}")


