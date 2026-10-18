#Windows
#.\.venv\Scripts\fastapi.exe dev Tema1-API-REST/02_get_por_id.py
#Linux o Mac
#./.venv/bin/fastapi dev 02_get_por_id.py

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