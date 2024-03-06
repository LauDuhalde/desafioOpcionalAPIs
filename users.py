##Se guarda data en variables indicadas en requerimientos, aunque no son utilizadas
import requests
import json
from access_users import *

# Verificar el código de estado de la respuesta

#1
users_data = get_users()

#2
new_user={
    "first_name": "Ignacio",
    "job":"Profesor"
}
    
created_user=users_data.copy()
create_user(new_user)
created_user = get_users()

#3 (no existe morpheus, así que actualicé a Emma)
updated_user=users_data.copy()
for user in updated_user:
    if user.get("first_name") == "Emma":
        user["residence"] = "zion"
        update_user(user["id"], user)
        break
updated_user = get_users()
    
#4    
remove_user=users_data.copy()
for user in remove_user:
    if user["first_name"] == "Tracey":
        delete_user(user["id"])
        break
remove_user = get_users()
    



