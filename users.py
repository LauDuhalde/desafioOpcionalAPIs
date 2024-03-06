##Solicitudes responden ok, pero realmente no actualizan los datos por lo que el get no refleja las operaciones
##Se imprimen variables JSON para "verificar"
import requests
import json


url="https://reqres.in/api/users"
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:
    print("La solicitud GET fue exitosa")
    #1
    users_data = response.json().get("data")
    print(users_data)
    print("--------------------------------------------\n")

    #2
    new_user={
        "first_name": "Ignacio",
        "job":"Profesor"
    }
    
    created_user=users_data.copy()
    #created_user.append(new_user)
    response = requests.post(url, json=new_user)
    if response.status_code == 201:
        print("La solicitud POST fue exitosa")
        created_user = requests.get(url).json().get("data")
    print(created_user)
    print("--------------------------------------------\n")

    #3 (no existe morpheus, así que actualicé a Emma)
    updated_user=users_data.copy()
    for user in updated_user:
        if user.get("first_name") == "Emma":
            user["residence"] = "zion"
            response = requests.put(url+"/"+str(user["id"]), json=user)
            if response.status_code == 200:
                print("La solicitud PUT fue exitosa")
                updated_user = requests.get(url).json().get("data")
            break
    print(updated_user)
    print("--------------------------------------------\n")
    
    #4    
    remove_user=users_data.copy()
    for user in remove_user:
        if user["first_name"] == "Tracey":
            response = requests.delete(url+"/"+str(user["id"]))
            if response.status_code == 204:
                print("La solicitud DELETE fue exitosa")
                remove_user = requests.get(url).json().get("data")
            break
    print(remove_user)
    print("--------------------------------------------\n")
    
elif response.status_code == 404:
    print("La solicitud GET falló: recurso no encontrado")
else:
    print(f"La solicitud GET falló con el código de estado {response.status_code}")


