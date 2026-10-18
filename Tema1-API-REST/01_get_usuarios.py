#Windows
#.\.venv\Scripts\fastapi.exe dev Tema1-API-REST/01_get_usuarios.py
#Linux o Mac
#./.venv/bin/fastapi dev 01_get_usuarios.py

from fastapi import FastAPI
from pydantic import BaseModel
#from pydantic import BaseModel, Field


app = FastAPI()

# Definimos cómo es un usuario

class User(BaseModel):
    name: str
    surname: str
    age: int
    #age: int = Field(ge=0, le=120)

# Lista de usuarios que simula una base de datos
users_list = [
    User(name="Paco", surname="Pérez", age=-5),
    User(name="María", surname="Martínez", age=20),
    User(name="Lucía", surname="Rodríguez", age=40)
]

#http://127.0.0.1:8000/users
# Operación para obtener todos los usuarios
@app.get("/users")
def users():
    return users_list