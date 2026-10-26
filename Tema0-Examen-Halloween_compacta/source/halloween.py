"""La feria de las sombras — funciones (solución compacta comentada)."""
import csv
from collections import namedtuple
from datetime import datetime

Visita = namedtuple('Visita', 'codigo,fecha,grupo,recorrido,personas,minutos,sustos,precio')


def leer_visitas(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # La primera línea contiene los nombres de las columnas.
        # Cada fila se transforma en una tupla nombrada; se convierten fecha y números.
        return [Visita(
            fila[0], datetime.strptime(fila[1], '%d/%m/%Y').date(),
            fila[2], fila[3], int(fila[4]), int(fila[5]),
            int(fila[6]), float(fila[7])
        ) for fila in lector]


def recaudacion(registros, recorrido):
    # Expresión generadora: produce cada importe válido sin crear otra lista.
    return sum(r.personas * r.precio for r in registros if r.recorrido == recorrido)


def visitas_rapidas(registros, sustos_minimos, duracion_maxima):
    # El generador selecciona solo códigos válidos; sorted devuelve una lista ordenada.
    return sorted(r.codigo for r in registros
                  if r.sustos >= sustos_minimos and r.minutos <= duracion_maxima)


def asistencia_por_recorrido(registros):
    # Conjunto por comprensión: recorridos únicos (sin repetir nombres).
    recorridos = {r.recorrido for r in registros}
    # Diccionario por comprensión: para cada recorrido, suma las personas de sus visitas.
    return {nombre: sum(r.personas for r in registros if r.recorrido == nombre)
            for nombre in recorridos}


def grupos_repetidores(registros):
    # Primer conjunto: nombres de los grupos sin duplicados.
    grupos = {r.grupo for r in registros}
    # Conjunto resultante: grupo que aparece en al menos dos recorridos DISTINTOS.
    # El conjunto interior elimina automáticamente las visitas repetidas al mismo recorrido.
    return {grupo for grupo in grupos
            if len({r.recorrido for r in registros if r.grupo == grupo}) >= 2}
