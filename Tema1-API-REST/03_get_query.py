#./.venv/bin/fastapi dev 03_get_query.py
#.\.venv\Scripts\fastapi.exe dev Tema1-API-REST/03_get_query.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int = Field(ge=0, le=120)

users_list = [
    User(id=1, name="Paco", surname="Pérez", age=30),
    User(id=2, name="María", surname="Martínez", age=20),
    User(id=3, name="Lucía", surname="Rodríguez", age=40)
]

#http://127.0.0.1:8000/users
@app.get("/users")
def users():
    return users_list

#http://127.0.0.1:8000/users/2
@app.get("/users/{id}")
def get_user(id: int):
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

#http://127.0.0.1:8000/users/?id=2
@app.get("/users/")
def get_user_query(id: int):
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

#http://127.0.0.1:8000/users/?id=hola da error 422 ya que el parametro debe ser entero

#ejemplo de varios parametros
#http://127.0.0.1:8000/buscar?nombre=Paco&edad=30
@app.get("/buscar")
def buscar(nombre: str, edad: int):
    return {
        "nombre_buscado": nombre,
        "edad_buscada": edad
    }

#http://127.0.0.1:8000/mayores?edad=25
@app.get("/mayores")
def usuarios_mayores(edad: int):
    # Completar
    return [ u for u in users_list if u.age>edad]

#también será válido
# @app.get("/mayores")
# def usuarios_mayores(edad: int):
#     resultado = []

#     for usuario in users_list:
#         if usuario.age > edad:
#             resultado.append(usuario)

#     return resultado