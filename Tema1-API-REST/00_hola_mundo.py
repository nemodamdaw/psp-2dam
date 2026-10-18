#.\.venv\Scripts\fastapi.exe dev Tema1-API-REST/00_hola_mundo.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

# GET http://127.0.0.1:8000/saludo/Paco
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": "Hola "+nombre}

# GET http://127.0.0.1:8000/saludo/Paco
# @app.get("/saludo/{nombre}")
# def saludar(nombre: str):
#     return {"saludo": f"Hola, {nombre}"}

# 