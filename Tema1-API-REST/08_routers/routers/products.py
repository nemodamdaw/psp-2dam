
# TEMA 1 - API REST
# Ejemplo 08: Router de productos
#
# Este archivo no se ejecuta directamente.
# Lo incorpora main.py mediante include_router().

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


# Modelo de producto.
class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)


# Lista de productos.
products_list = [
    Product(id=1, name="Teclado", price=25.50),
    Product(id=2, name="Ratón", price=15.99),
    Product(id=3, name="Monitor", price=189.90)
]


# GET http://127.0.0.1:8000/products
# Devuelve todos los productos.
@router.get("")
def obtener_productos():
    return products_list


# GET http://127.0.0.1:8000/products/2
# Devuelve un producto por su ID.
@router.get("/{id}")
def obtener_producto(id: int):

    for producto in products_list:
        if producto.id == id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )
