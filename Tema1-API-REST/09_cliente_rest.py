
# TEMA 1 - API REST
# Ejemplo 09: Cliente REST con requests
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 09_cliente_rest.py
#
# Antes debemos arrancar el servidor:
# ./.venv/bin/fastapi dev 08_routers/main.py

import requests

URL = "http://127.0.0.1:8000"


# -------------------------------------------
# PETICIÓN GET - LISTAR USUARIOS
# -------------------------------------------

# GET http://127.0.0.1:8000/users

respuesta = requests.get(f"{URL}/users", timeout=5)

print("GET /users")
print("Código HTTP:", respuesta.status_code)
print("Usuarios:", respuesta.json())


# -------------------------------------------
# PETICIÓN GET - BUSCAR UN USUARIO
# -------------------------------------------

# GET http://127.0.0.1:8000/users/2

respuesta = requests.get(f"{URL}/users/2", timeout=5)

print("\nGET /users/2")
print("Código HTTP:", respuesta.status_code)
print("Usuario:", respuesta.json())


# -------------------------------------------
# PETICIÓN POST - CREAR UN USUARIO
# -------------------------------------------

# POST http://127.0.0.1:8000/users

nuevo_usuario = {
    "name": "Laura",
    "surname": "Gómez",
    "age": 24
}

respuesta = requests.post(
    f"{URL}/users",
    json=nuevo_usuario,
    timeout=5
)

print("\nPOST /users")
print("Código HTTP:", respuesta.status_code)
print("Usuario creado:", respuesta.json())


# -------------------------------------------
# PETICIÓN GET - COMPROBAR EL RESULTADO
# -------------------------------------------

# GET http://127.0.0.1:8000/users

respuesta = requests.get(f"{URL}/users", timeout=5)

print("\nGET /users después del POST")
print("Usuarios:", respuesta.json())
