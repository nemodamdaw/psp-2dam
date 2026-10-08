from olimpiadas import *


def test_lee_olimpiadas(registros):
    print()
    print("test_lee_olimpiadas")
    print('\tLeidos',len(registros),'registros')
    print('\tMostrando los tres primeros:')
    #print(registros[:3])
    cont=0
    for r in registros:
        print("\t",r)
        cont+=1
        if cont>=3:
            break
    print()

def test_edad_media(registros):
    print()
    print("test_edad_media")
    print('\tLa edad media de los atletas es:',edad_media(registros))
    print()

def test_num_atletas_por_pais(registros):
    print()
    print("test_num_atletas_por_pais")
    d=num_atletas_por_pais(registros)
    #print('num atletas por pais:',num_atletas_por_pais(registros))
    for parejita in d.items():
        print("\t",parejita[0],"-->",parejita[1])
    print()

def test_nombre_atletas_por_pais(registros):
    print()
    print("test_nombre_atletas_por_pais")
    d=nombre_atletas_por_pais(registros)
    for parejita in d.items():
        print("\t",parejita[0],"-->",parejita[1])
    print()

if __name__ == "__main__":
    print('Olimpiadas')
    registros=leer_olimpiadas('./Tema0-Practica1-Olimpiadas/data/atletas.txt')
    test_lee_olimpiadas(registros)
    test_edad_media(registros)
    test_num_atletas_por_pais(registros)
    test_nombre_atletas_por_pais(registros)
    print(atleta_mayor_peso(registros))
    print(pais_mayor_peso_medio(registros))
    print(metodozip(registros))


