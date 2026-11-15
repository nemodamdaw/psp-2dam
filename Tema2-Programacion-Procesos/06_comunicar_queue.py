# Ejemplo 06 - Los hijos envían sus resultados a una cola
import multiprocessing


def calcular_cuadrado(numero, cola):
    resultado = numero * numero
    cola.put((numero, resultado))


if __name__ == "__main__":
    cola = multiprocessing.Queue()
    procesos = []

    for numero in (2, 3, 4):
        p = multiprocessing.Process(target=calcular_cuadrado, args=(numero, cola))
        procesos.append(p)
        p.start()

    for _ in procesos:
        numero, resultado = cola.get()
        print(f"{numero} al cuadrado = {resultado}")

    for p in procesos:
        p.join()
