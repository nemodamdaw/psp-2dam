
# TEMA 1 - API REST
# Ejemplo 06: GET, POST, PUT y PATCH
#
# Para ejecutar:
# ./.venv/bin/fastapi dev 06_patch_usuarios.py
#
# Documentación interactiva:
# http://127.0.0.1:8000/docs
#
# GET: Consulta usuarios.
# POST: Crea usuarios nuevos.
# PUT: Modifica completamente un usuario.
# PATCH: Modifica parcialmente un usuario.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# -------------------------------------------
# MODELOS DE DATOS
# -------------------------------------------

# Modelo para crear o sustituir usuarios.
class UserCreate(BaseModel):
    name: str
    surname: str
    age: int = Field(ge=0, le=120)


# Modelo del usuario completo, con ID.
class User(UserCreate):
    id: int


# NUEVO: Modelo para modificaciones parciales.
# Todos los atributos son opcionales.
class UserPatch(BaseModel):
    name: str | None = None
    surname: str | None = None
    age: int | None = Field(default=None, ge=0, le=120)


# -------------------------------------------
# LISTA QUE SIMULA UNA BASE DE DATOS
# -------------------------------------------

users_list = [
    User(id=1, name="Paco", surname="Pérez", age=30),
    User(id=2, name="María", surname="Martínez", age=20),
    User(id=3, name="Lucía", surname="Rodríguez", age=40)
]


# -------------------------------------------
# FUNCIÓN AUXILIAR
# -------------------------------------------

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
# Consulta mediante un parámetro query.
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
# Devuelve usuarios mayores que la edad indicada.
@app.get("/mayores")
def usuarios_mayores(edad: int):
    return [u for u in users_list if u.age > edad]


# -------------------------------------------
# OPERACIÓN POST
# -------------------------------------------

# POST http://127.0.0.1:8000/users
# Probar desde http://127.0.0.1:8000/docs
# Crea un usuario nuevo.
@app.post("/users", status_code=201, response_model=User)
def crear_usuario(usuario: UserCreate):

    siguiente_id = max(
        (u.id for u in users_list),
        default=0
    ) + 1

    nuevo_usuario = User(
        id=siguiente_id,
        name=usuario.name,
        surname=usuario.surname,
        age=usuario.age
    )

    # Alternativa:
    # nuevo_usuario = User(
    #     id=siguiente_id,
    #     **usuario.model_dump()
    # )

    users_list.append(nuevo_usuario)

    return nuevo_usuario


# -------------------------------------------
# OPERACIÓN PUT
# -------------------------------------------

# PUT http://127.0.0.1:8000/users/2
# Probar desde http://127.0.0.1:8000/docs
# Modifica completamente un usuario existente.
@app.put("/users/{id}", response_model=User)
def modificar_usuario(id: int, datos: UserCreate):

    for posicion, usuario in enumerate(users_list):

        if usuario.id == id:

            usuario_modificado = User(
                id=id,
                name=datos.name,
                surname=datos.surname,
                age=datos.age
            )

            # Alternativa:
            # usuario_modificado = User(
            #     id=id,
            #     **datos.model_dump()
            # )

            users_list[posicion] = usuario_modificado

            return usuario_modificado

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# -------------------------------------------
# OPERACIÓN PATCH - NUEVA
# -------------------------------------------

# PATCH http://127.0.0.1:8000/users/2
# Probar desde http://127.0.0.1:8000/docs
# Modifica solamente los atributos enviados.
@app.patch("/users/{id}", response_model=User)
def modificar_usuario_parcial(id: int, datos: UserPatch):

    # Buscamos al usuario y su posición.
    for posicion, usuario in enumerate(users_list):

        if usuario.id == id:

            # Obtenemos solo los campos enviados
            # y con valor diferente de None.
            cambios = datos.model_dump(
                exclude_unset=True,
                exclude_none=True
            )

            # Partimos de los datos originales.
            datos_actualizados = usuario.model_dump()

            # Sustituimos solo los campos enviados.
            datos_actualizados.update(cambios)

            # Creamos el usuario actualizado,
            # validando de nuevo sus atributos.
            usuario_modificado = User(
                **datos_actualizados
            )

            # Sustituimos el usuario en la lista.
            users_list[posicion] = usuario_modificado

            return usuario_modificado

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
