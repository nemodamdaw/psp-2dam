
# TEMA 1 - API REST
# Ejemplo 08: Router de usuarios
#
# Este archivo no se ejecuta directamente.
# Lo incorpora main.py mediante include_router().
#
# Documentación:
# http://127.0.0.1:8000/docs

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Creamos el router de usuarios.
router = APIRouter()


# -------------------------------------------
# MODELOS DE DATOS
# -------------------------------------------

class UserCreate(BaseModel):
    name: str
    surname: str
    age: int = Field(ge=0, le=120)


class User(UserCreate):
    id: int


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
    for usuario in users_list:
        if usuario.id == id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# -------------------------------------------
# OPERACIONES GET
# -------------------------------------------

# GET http://127.0.0.1:8000/users
# Devuelve todos los usuarios.
@router.get("")
def obtener_usuarios():
    return users_list


# GET http://127.0.0.1:8000/users/?id=2
# Busca un usuario mediante parámetro de consulta.
@router.get("/")
def obtener_usuario_query(id: int):
    return buscar_usuario(id)


# GET http://127.0.0.1:8000/users/buscar?nombre=Paco&edad=30
# Recibe dos parámetros de consulta.
@router.get("/buscar")
def buscar(nombre: str, edad: int):
    return {
        "nombre_buscado": nombre,
        "edad_buscada": edad
    }


# GET http://127.0.0.1:8000/users/mayores?edad=25
# Devuelve usuarios mayores que la edad indicada.
@router.get("/mayores")
def usuarios_mayores(edad: int):
    return [u for u in users_list if u.age > edad]


# GET http://127.0.0.1:8000/users/2
# Devuelve un usuario por su ID.
@router.get("/{id}")
def obtener_usuario(id: int):
    return buscar_usuario(id)


# -------------------------------------------
# OPERACIÓN POST
# -------------------------------------------

# POST http://127.0.0.1:8000/users
# Probar desde http://127.0.0.1:8000/docs
# Crea un usuario nuevo.
@router.post("", status_code=201, response_model=User)
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
# Sustituye todos los datos editables del usuario.
@router.put("/{id}", response_model=User)
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
# OPERACIÓN PATCH
# -------------------------------------------

# PATCH http://127.0.0.1:8000/users/2
# Probar desde http://127.0.0.1:8000/docs
# Modifica solamente los atributos enviados.
@router.patch("/{id}", response_model=User)
def modificar_usuario_parcial(id: int, datos: UserPatch):

    for posicion, usuario in enumerate(users_list):

        if usuario.id == id:

            cambios = datos.model_dump(
                exclude_unset=True,
                exclude_none=True
            )

            datos_actualizados = usuario.model_dump()

            datos_actualizados.update(cambios)

            usuario_modificado = User(
                **datos_actualizados
            )

            users_list[posicion] = usuario_modificado

            return usuario_modificado

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# -------------------------------------------
# OPERACIÓN DELETE
# -------------------------------------------

# DELETE http://127.0.0.1:8000/users/2
# Probar desde http://127.0.0.1:8000/docs
# Elimina un usuario por su ID.
@router.delete("/{id}")
def eliminar_usuario(id: int):

    for usuario in users_list:

        if usuario.id == id:

            # Eliminamos directamente el objeto.
            users_list.remove(usuario)

            return {}

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
