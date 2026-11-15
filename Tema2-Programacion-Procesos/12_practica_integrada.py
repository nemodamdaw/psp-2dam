# Ejemplo 12 - Varios procesos calculan las ventas de distintas sucursales
import multiprocessing
import os


def calcular_ventas(sucursal, importes, resultados):
    total = sum(importes)
    resultados.put((sucursal, total, os.getpid()))


if __name__ == "__main__":
    ventas = {
        "Nervión": [25, 40, 15],
        "Triana": [20, 50, 10],
        "Macarena": [30, 10, 45]
    }

    resultados = multiprocessing.Queue()
    procesos = []

    for sucursal, importes in ventas.items():
        p = multiprocessing.Process(
            target=calcular_ventas,
            args=(sucursal, importes, resultados)
        )
        procesos.append(p)
        p.start()

    total_general = 0
    for _ in procesos:
        sucursal, total, pid = resultados.get()
        print(f"{sucursal}: {total} euros (PID {pid})")
        total_general += total

    for p in procesos:
        p.join()

    print("Recaudación general:", total_general, "euros")
