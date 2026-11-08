"""La feria de las sombras — funciones del examen (solución clásica)."""
import csv
from collections import namedtuple
from datetime import datetime

Visita = namedtuple('Visita', 'codigo,fecha,grupo,recorrido,personas,minutos,sustos,precio')


def leer_visitas(ruta):
    registros = []
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            codigo = linea[0]
            fecha = datetime.strptime(linea[1], '%d/%m/%Y').date()
            grupo = linea[2]
            recorrido = linea[3]
            personas = int(linea[4])
            minutos = int(linea[5])
            sustos = int(linea[6])
            precio = float(linea[7])
            tupla = Visita(codigo, fecha, grupo, recorrido, personas, minutos, sustos, precio)
            registros.append(tupla)
    return registros


def recaudacion(registros, recorrido):
    total = 0.0
    for r in registros:
        if r.recorrido == recorrido:
            total += r.personas * r.precio
    return total


def visitas_rapidas(registros, sustos_minimos, duracion_maxima):
    lis = []
    for r in registros:
        if r.sustos >= sustos_minimos and r.minutos <= duracion_maxima:
            lis.append(r.codigo)
    return sorted(lis)


def asistencia_por_recorrido(registros):
    d = {}
    for r in registros:
        clave = r.recorrido
        if clave in d:
            d[clave] += r.personas
        else:
            d[clave] = r.personas
    return d


def grupos_repetidores(registros):
    d = {}
    for r in registros:
        clave = r.grupo
        if clave in d:
            d[clave].add(r.recorrido)
        else:
            d[clave] = {r.recorrido}

    resultado = set()
    for clave in d:
        if len(d[clave]) >= 2:
            resultado.add(clave)
    return resultado
