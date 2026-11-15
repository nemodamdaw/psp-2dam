# Ejemplo 03 - Diferencia entre esperar al final y esperar pronto
import multiprocessing
import time


def tarea(nombre):
    print(f"Empieza {nombre}", flush=True)
    time.sleep(1)
    print(f"Termina {nombre}", flush=True)


if __name__ == "__main__":
    inicio = time.perf_counter()
    p1 = multiprocessing.Process(target=tarea, args=("A",))
    p2 = multiprocessing.Process(target=tarea, args=("B",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Tiempo total: {time.perf_counter() - inicio:.2f} s")
