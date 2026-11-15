# Ejemplo 11 - Comprobar cómo termina un proceso
import multiprocessing
import time


def trabajar():
    time.sleep(0.5)
    print("Trabajo completado", flush=True)


if __name__ == "__main__":
    proceso = multiprocessing.Process(target=trabajar, name="Trabajador")
    proceso.start()
    print("Nombre:", proceso.name)
    print("PID:", proceso.pid)
    print("¿Sigue vivo?:", proceso.is_alive())
    print("Código antes de esperar:", proceso.exitcode)
    proceso.join()
    print("¿Sigue vivo?:", proceso.is_alive())
    print("Código al terminar:", proceso.exitcode)
