
# TEMA 1 - API REST
# Ejemplo 05: GET, POST y PUT
#
# Para ejecutar este ejemplo:
# ./.venv/bin/fastapi dev 05_put_usuarios.py
#
# Documentación interactiva:
# http://127.0.0.1:8000/docs
#
# GET: Consulta usuarios.
# POST: Crea usuarios nuevos.
# PUT: Modifica completamente un usuario existente.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# MODELOS DE DATOS

# Modelo para crear o modificar usuarios: sin ID
class UserCreate(BaseModel):
    name: str
    surname: str
    age: int = Field(ge=0, le=120)


# Modelo del usuario completo: con ID
class User(UserCreate):
    id: int


# LISTA QUE SIMULA UNA BASE DE DATOS

users_list = [
    User(id=1, name="Paco", surname="Pérez", age=30),
    User(id=2, name="María", surname="Martínez", age=20),
    User(id=3, name="Lucía", surname="Rodríguez", age=40)
]


# FUNCIÓN AUXILIAR PARA BUSCAR UN USUARIO

def buscar_usuario(id: int):
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# -------------------------------------------
# OPERACIONES GET
# -------------------------------------------

# GET http://127.0.0.1:8000/users
# Devuelve todos los usuarios.
@app.get("/users")
def obtener_usuarios():
    return users_list


# GET http://127.0.0.1:8000/users/2
# Devuelve un usuario por su ID.
@app.get("/users/{id}")
def obtener_usuario(id: int):
    return buscar_usuario(id)


# GET http://127.0.0.1:8000/users/?id=2
# Consulta mediante un parámetro de tipo query.
@app.get("/users/")
def obtener_usuario_query(id: int):
    return buscar_usuario(id)


# GET http://127.0.0.1:8000/buscar?nombre=Paco&edad=30
# Recibe dos parámetros de consulta.
@app.get("/buscar")
def buscar(nombre: str, edad: int):
    return {
        "nombre_buscado": nombre,
        "edad_buscada": edad
    }


# GET http://127.0.0.1:8000/mayores?edad=25
# Devuelve usuarios cuya edad sea mayor que la indicada.
@app.get("/mayores")
def usuarios_mayores(edad: int):
    return [u for u in users_list if u.age > edad]


# -------------------------------------------
# OPERACIÓN POST
# -------------------------------------------

# POST http://127.0.0.1:8000/users
# Se prueba desde http://127.0.0.1:8000/docs
# Crea un usuario nuevo.
@app.post("/users", status_code=201, response_model=User)
def crear_usuario(usuario: UserCreate):

    # Calculamos el siguiente identificador.
    siguiente_id = max(
        (u.id for u in users_list),
        default=0
    ) + 1

    # Creamos el usuario con su nuevo ID.
    nuevo_usuario = User(
        id=siguiente_id,
        name=usuario.name,
        surname=usuario.surname,
        age=usuario.age
    )

    # Otra forma: desempaquetando un diccionario.
    # nuevo_usuario = User(
    #     id=siguiente_id,
    #     **usuario.model_dump()
    # )

    # Añadimos el nuevo usuario a la lista.
    users_list.append(nuevo_usuario)

    # Devolvemos el usuario creado.
    return nuevo_usuario


# -------------------------------------------
# OPERACIÓN PUT
# -------------------------------------------

# PUT http://127.0.0.1:8000/users/2
# Se prueba desde http://127.0.0.1:8000/docs
# Modifica completamente un usuario existente.
@app.put("/users/{id}", response_model=User)
def modificar_usuario(id: int, datos: UserCreate):

    # Recorremos la lista obteniendo posición y usuario.
    for posicion, usuario in enumerate(users_list):

        # Comprobamos si es el usuario que buscamos.
        if usuario.id == id:

            # Creamos el usuario con los nuevos datos.
            usuario_modificado = User(
                id=id,
                name=datos.name,
                surname=datos.surname,
                age=datos.age
            )

            # Otra forma: desempaquetando un diccionario.
            # usuario_modificado = User(
            #     id=id,
            #     **datos.model_dump()
            # )

            # Sustituimos el usuario anterior.
            users_list[posicion] = usuario_modificado

            # Devolvemos el usuario modificado.
            return usuario_modificado

    # Si el usuario no existe, devolvemos error 404.
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
