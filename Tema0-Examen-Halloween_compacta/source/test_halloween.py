"""Pruebas del examen Halloween. Ejecutar este archivo (contiene el main)."""
from pathlib import Path
from datetime import date
from halloween import (leer_visitas, recaudacion, visitas_rapidas,
                       asistencia_por_recorrido, grupos_repetidores)

# Se obtiene el fichero tomando como base la ubicación del proyecto.
FICHERO = Path(__file__).resolve().parent.parent / 'data' / 'visitas_halloween.txt'


def test_lectura(visitas):
    print('Ejercicio 1 · Registros leídos:', len(visitas))
    print('Primera visita:', visitas[0])
    assert len(visitas) == 24
    assert visitas[0].codigo == 'H001'
    assert visitas[0].fecha == date(2026, 10, 22)
    assert leer_visitas(str(FICHERO)) == visitas


def test_recaudacion(visitas):
    total = recaudacion(visitas, 'Cripta')
    print('Ejercicio 2 · Recaudación Cripta:', total)
    assert total == 170.0
    assert recaudacion(visitas, 'Mansión') == 0


def test_visitas_rapidas(visitas):
    codigos = visitas_rapidas(visitas, 30, 29)
    print('Ejercicio 3 · Visitas rápidas:', codigos)
    assert codigos == ['H001', 'H008', 'H009', 'H011', 'H014', 'H016']
    assert visitas_rapidas(visitas, 999, 1) == []


def test_asistencia_por_recorrido(visitas):
    resultado = asistencia_por_recorrido(visitas)
    print('Ejercicio 4 · Asistencia:', resultado)
    assert resultado == {'Cripta': 34, 'Bosque': 27,
                         'Laberinto': 32, 'Castillo': 33}


def test_grupos_repetidores(visitas):
    resultado = grupos_repetidores(visitas)
    print('Ejercicio 5 · Grupos que repiten:', sorted(resultado))
    assert resultado == {'Arañas', 'Brujas', 'Calabazas', 'Cuervos',
                         'Esqueletos', 'Fantasmillas', 'Murcielagos', 'Sombras'}
    assert grupos_repetidores([]) == set()


if __name__ == '__main__':
    visitas = leer_visitas(str(FICHERO))
    test_lectura(visitas)
    test_recaudacion(visitas)
    test_visitas_rapidas(visitas)
    test_asistencia_por_recorrido(visitas)
    test_grupos_repetidores(visitas)
    print('Todas las pruebas se han superado.')
