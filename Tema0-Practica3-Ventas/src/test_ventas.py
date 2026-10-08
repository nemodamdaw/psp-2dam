from ventas import *

def test_leer(registros):
    print('Leidos',len(registros))
    print(registros[:2])
    print()


registros=leer('./Tema0-Practica3-Ventas/data/ventas.txt')
test_leer(registros)
print(clientes_producto1_y_producto2(registros,'ProductoC','ProductoB'))
conj={'ProductoA','ProductoB'}
print(clientes_producto1_y_producto2Otro(registros,conj))
print(diccionario_porcentaje_cantidad_producto(registros))
nombres={'ClienteA','ClienteB'}
print(producto_mas_vendido(registros,nombres,3))