# Ejemplo 08 - Dos procesos modifican un valor compartido
import multiprocessing


def duplicar(valor):
    with valor.get_lock():
        valor.value *= 2


if __name__ == "__main__":
    numero = multiprocessing.Value("i", 5)
    print("Antes:", numero.value)
    p1 = multiprocessing.Process(target=duplicar, args=(numero,))
    p2 = multiprocessing.Process(target=duplicar, args=(numero,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Después:", numero.value)
