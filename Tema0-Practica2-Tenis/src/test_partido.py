from partido import *

def test_lee_fichero(registros):
    print()
    print('Test lectura de fichero')
    for r in registros:
        print(r)
    print()
def test_diccionario_diferencia_juegos_superficie(registros):
    print()
    print('Test diccionario_diferencia_juegos_superficie')
    d=diccionario_diferencia_juegos_superficie(registros,3)
    for clave in d:
        print(clave,': ', d[clave])
    print()
if __name__ == "__main__":
    registros = lee_fichero('./Tema0-Practica2-Tenis/data/datos.txt')
    test_lee_fichero(registros)
    print()
    print('***************************')
    print(desviaciones_media(registros,5))
    print()
    print('***************************')
    #print( diccionario_diferencia_juegos_superficie(registros,3) )
    test_diccionario_diferencia_juegos_superficie(registros)
    print()
    print('***************************')
    print(rival_mayor_porcentaje_victorias(registros, 'Tierra'))