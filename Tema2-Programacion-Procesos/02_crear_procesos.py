# Ejemplo 02 - Dos procesos independientes
import multiprocessing
import os
import time


def tarea(nombre):
    for numero in range(1, 4):
        print(f"{nombre} (PID {os.getpid()}): paso {numero}", flush=True)
        time.sleep(0.4)


if __name__ == "__main__":
    inicio = time.perf_counter()
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea A",))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea B",))
    proceso1.start()
    proceso2.start()
    print(f"Arrancados los procesos {proceso1.pid} y {proceso2.pid}")
    proceso1.join()
    proceso2.join()
    print(f"Duración: {time.perf_counter() - inicio:.2f} s")
