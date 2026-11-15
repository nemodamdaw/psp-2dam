# Ejemplo 04 - Cada proceso recibe sus propios datos
import multiprocessing


def mostrar_tabla(numero):
    for factor in range(1, 6):
        print(f"{numero} x {factor} = {numero * factor}", flush=True)


if __name__ == "__main__":
    procesos = []
    for numero in (3, 5, 7):
        proceso = multiprocessing.Process(target=mostrar_tabla, args=(numero,))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    print("Todas las tablas terminadas")
