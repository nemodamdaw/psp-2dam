# Ejemplo 01 - Dos tareas ejecutadas una detrás de otra
import time


def tarea(nombre):
    for numero in range(1, 4):
        print(f"{nombre}: paso {numero}")
        time.sleep(0.4)


if __name__ == "__main__":
    inicio = time.perf_counter()
    tarea("Tarea A")
    tarea("Tarea B")
    duracion = time.perf_counter() - inicio
    print(f"Duración secuencial: {duracion:.2f} s")
