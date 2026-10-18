# Para ejecutar este ejemplo desde la terminal:
# ./.venv/bin/fastapi dev 04_post_usuarios.py
#
# Documentación interactiva:
# http://127.0.0.1:8000/docs
#
# - GET /users: obtiene la lista de usuarios.
# - POST /users: añade un usuario a la lista.
# las dos operaciones utilizan la misma URL, pero se distinguen por el método HTTP.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# Modelo para crear usuarios: sin ID
class UserCreate(BaseModel):
    name: str
    surname: str
    age: int = Field(ge=0, le=120)


# Modelo del usuario completo: con ID
class User(UserCreate):
    id: int


# Lista que simula una base de datos
users_list = [
    User(id=1, name="Paco", surname="Pérez", age=30),
    User(id=2, name="María", surname="Martínez", age=20),
    User(id=3, name="Lucía", surname="Rodríguez", age=40)
]


# Función auxiliar para buscar un usuario
def buscar_usuario(id: int):
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# GET http://127.0.0.1:8000/users
@app.get("/users")
def obtener_usuarios():
    return users_list


# GET http://127.0.0.1:8000/users/2
@app.get("/users/{id}")
def obtener_usuario(id: int):
    return buscar_usuario(id)


# GET http://127.0.0.1:8000/users/?id=2
@app.get("/users/")
def obtener_usuario_query(id: int):
    return buscar_usuario(id)


# GET http://127.0.0.1:8000/buscar?nombre=Paco&edad=30
@app.get("/buscar")
def buscar(nombre: str, edad: int):
    return {
        "nombre_buscado": nombre,
        "edad_buscada": edad
    }


# GET http://127.0.0.1:8000/mayores?edad=25
@app.get("/mayores")
def usuarios_mayores(edad: int):
    return [u for u in users_list if u.age > edad]


# POST http://127.0.0.1:8000/users
# Se prueba desde http://127.0.0.1:8000/docs
@app.post("/users", status_code=201, response_model=User)
def crear_usuario(usuario: UserCreate):

    # Calculamos el siguiente identificador
    siguiente_id = max(
        (u.id for u in users_list),
        default=0
    ) + 1

    # Creamos el usuario con su nuevo ID
    nuevo_usuario = User(
            id=siguiente_id,
            name = usuario.name,
            surname = usuario.surname,
            age = usuario.age
    )
    
    #de otra forma (Segunda forma: desempaquetar un diccionario)
    # nuevo_usuario = User(
    #     id=siguiente_id,
    #     **usuario.model_dump()
    # )

    # Lo añadimos a nuestra lista
    users_list.append(nuevo_usuario)

    # Devolvemos el usuario creado
    return nuevo_usuario