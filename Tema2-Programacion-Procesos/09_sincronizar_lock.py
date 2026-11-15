# Ejemplo 09 - Incrementar un contador compartido con Lock
import multiprocessing


def sumar(contador, bloqueo, repeticiones):
    for _ in range(repeticiones):
        with bloqueo:
            contador.value += 1


if __name__ == "__main__":
    contador = multiprocessing.Value("i", 0)
    bloqueo = multiprocessing.Lock()
    procesos = []

    for _ in range(3):
        p = multiprocessing.Process(target=sumar, args=(contador, bloqueo, 1000))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Resultado esperado: 3000")
    print("Resultado obtenido:", contador.value)
