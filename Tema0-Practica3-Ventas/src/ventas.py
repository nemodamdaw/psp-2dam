from collections import namedtuple
import csv
from datetime import datetime


Venta = namedtuple('Venta', 'id,fecha,cliente,producto,cantidad,precio,beneficio')

#2051, 04/06/2019, ClienteB, ProductoC, 11, 7.60, 2.67
def leer(nombre):
    registros=[]
    with open(nombre, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            id = linea[0].strip()
            fecha = datetime.strptime(linea[1].strip(),'%d/%m/%Y').date()
            cliente = linea[2].strip()
            producto = linea[3].strip()
            cantidad = int(linea[4].strip())
            precio = float(linea[5].strip())
            beneficio = float(linea[6].strip())
            tupla=Venta(id,fecha,cliente,producto,cantidad,precio,beneficio)
            registros.append(tupla)
    return registros

def clientes_producto1_y_producto2(registros, p1, p2):
    cliep1={ r.cliente for r in registros if r.producto==p1}
    cliep2={ r.cliente for r in registros if r.producto==p2}
    return cliep1&cliep2

def clientes_producto1_y_producto2Otro(registros, conj):
    lis=list(conj)
    cliep1={ r.cliente for r in registros if r.producto==lis[0]}
    cliep2={ r.cliente for r in registros if r.producto==lis[1]}
    return cliep1&cliep2

# def diccionario_porcentaje_cantidad_producto(registros):
#     res={}
#     total=sum([r.cantidad for r in registros])
#     d1={}
#     for r in registros:
#         clave=r.producto
#         if clave in d1:
#             d1[clave]+=r.cantidad
#         else:
#             d1[clave]=r.cantidad
    
#     for clave in d1:
#         res[clave]=d1[clave]/total*100.0
#     return res

# def diccionario_porcentaje_cantidad_producto(registros):
#     res={}
#     total=sum([r.cantidad for r in registros])
#     d1=cantidad_por_producto(registros)
#     for clave in d1:
#         res[clave]=d1[clave]/total*100.0
#     return res

# def cantidad_por_producto(registros):
#     d1={}
#     for r in registros:
#         clave=r.producto
#         if clave in d1:
#             d1[clave]+=r.cantidad
#         else:
#             d1[clave]=r.cantidad
#     return d1

def diccionario_porcentaje_cantidad_producto(registros):
    res={}
    total=sum([r.cantidad for r in registros])
    d1 = auxiliar(registros)
    
    for clave in d1:
        res[clave]=d1[clave]/total*100.0
    return res

def auxiliar(registros):
    d1={}
    for r in registros:
        clave=r.producto
        if clave in d1:
            d1[clave]+=r.cantidad
        else:
            d1[clave]=r.cantidad
    return d1

# producto_mas_vendido: recibe una lista de tuplas de tipo Venta, un conjunto de nombres 
# de clientes y un número entero n, y devuelve el nombre del producto más frecuente de 
# entre las n compras con mayor cantidad de unidades de los clientes del conjunto. 
# El parámetro n tendrá un valor por defecto igual a 3. (4 puntos)

def producto_mas_vendido(registros, nombres, n=3):
    lis=n_compras_mayor_cant_en_nombres(registros, nombres, n)
    d=hacer_dicc_frec_prod(lis)
    return max(d.items(),key=lambda t:t[1])[0]

def n_compras_mayor_cant_en_nombres(registros, nombres, n=3):
    filtro=[r for r in registros if r.cliente in nombres]
    filtro=sorted(filtro,reverse=True,key= lambda t:t.cantidad)
    return filtro[:n]

def hacer_dicc_frec_prod(lis):
    d1={}
    for r in lis:
        clave=r.producto
        if clave in d1:
            d1[clave]+=1
        else:
            d1[clave]=1
    
    return d1
