##Solicitudes responden ok, pero realmente no actualizan los datos por lo que el get no refleja las operaciones
import requests
import json

url="https://reqres.in/api/users"
def get_users():
    response = requests.get(url)
    data = response.json().get("data")
    if response.status_code == 200:
        print("La solicitud GET fue exitosa")
        print(data)
        print("--------------------------------------------\n")
    elif response.status_code == 404:
        print("La solicitud GET falló: recurso no encontrado")
    else:
        print(f"La solicitud GET falló con el código de estado {response.status_code}")
    return data

def create_user(new_user):
    response = requests.post(url, json=new_user)
    if response.status_code == 201:
        print("La solicitud POST fue exitosa, ID Nuevo usuario:",response.json().get("id"))
    else:
        print("Error")

def update_user(id, user):
    response = requests.put(url+"/"+str(id), json=user)
    if response.status_code == 200:
            print("La solicitud PUT fue exitosa")
    else:
        print("Error")

def delete_user(id):
    response = requests.delete(url+"/"+str(id))
    if response.status_code == 204:
        print("La solicitud DELETE fue exitosa")
    else:
        print("Error")