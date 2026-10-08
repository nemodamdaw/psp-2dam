import csv
from collections import namedtuple
from datetime import datetime

Partido = namedtuple('Partido', 'fecha, rival, superficie, duracion,juegos_ganados, juegos_perdidos, ganado')
#11/10/2020,Novak Djokovic,Tierra,160,19,7,True
def lee_fichero(fichero):
    registros=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            fecha = datetime.strptime( linea[0], '%d/%m/%Y').date()
            rival = linea[1]
            superficie = linea[2]
            duracion = int(linea[3])
            juegos_ganados = int(linea[4])
            juegos_perdidos = int(linea[5])
            ganado = False
            if linea[6]=='True':
                ganado = True
            tupla = Partido(fecha, rival, superficie, duracion,juegos_ganados, juegos_perdidos, ganado)
            registros.append(tupla)

    return registros

def desviaciones_media(registros, n):
    minutos = [r.duracion for r in registros]
    media = sum(minutos)/len(minutos)
    return [ (r.duracion-media,r) for r in registros if r.duracion>=media+n]

def diccionario_diferencia_juegos_superficie(registros, n=3):
    d1 = {}
    for r in registros:
        clave = r.superficie
        if clave in d1:
            d1[clave] += [r]
        else:
            d1[clave] = [r]
    d2 = {}
    for clave in d1:
        d2[clave] = auxiliar( d1[clave],n)
    return d2

def auxiliar(lista, n):
    lista = sorted(lista,reverse=True, key=lambda t:t.juegos_ganados - t.juegos_perdidos )
    lista = lista[:n]
    return [r.fecha for r in lista]

def rival_mayor_porcentaje_victorias(registros, superficie):
    d1={}
    for r in registros:
        if r.superficie == superficie:
            clave = r.rival
            if clave in d1:
                #d1[clave] = d1[clave] + 1
                d1[clave] += 1
            else:
                d1[clave] = 1

    d2={}
    for r in registros:
        if r.superficie == superficie and r.ganado:
            clave = r.rival
            if clave in d2:
                d2[clave] += 1
            else:
                d2[clave] = 1

    d3={}
    for clave in d1:
        d3[clave] =100.0 * d2[clave]/d1[clave]

    return max(d3.items(), key = lambda t:t[1])