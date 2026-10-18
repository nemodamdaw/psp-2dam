
# TEMA 1 - API REST
# Ejemplo 08: Organización mediante routers
#
# Para ejecutar:
# ./.venv/bin/fastapi dev 08_routers/main.py
#
# Documentación interactiva:
# http://127.0.0.1:8000/docs

from fastapi import FastAPI
from routers import users, products

# Creamos la aplicación principal.
app = FastAPI(title="Ejemplo 08 - Routers")

# Incorporamos los routers a nuestra aplicación.
app.include_router(
    users.router,
    prefix="/users",
    tags=["Usuarios"]
)

app.include_router(
    products.router,
    prefix="/products",
    tags=["Productos"]
)


# GET http://127.0.0.1:8000/
@app.get("/")
def inicio():
    return {"mensaje": "API REST con routers"}
