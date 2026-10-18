
# TEMA 1 - API REST Y COMUNICACIÓN EN RED
# Ejemplo 13 - INTRODUCCIÓN A LOS HILOS
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 13_introduccion_hilos.py
#
# Compararemos la ejecución secuencial
# con la ejecución concurrente mediante hilos.

import threading
import time


# -------------------------------------------
# FUNCIÓN QUE SIMULA UNA TAREA
# -------------------------------------------

def tarea(nombre):

    for i in range(1, 4):

        print(f"{nombre}: paso {i}")

        # Simulamos una operación que tarda un segundo.
        time.sleep(1)

    print(f"{nombre}: terminado")


# -------------------------------------------
# PRIMERA PARTE: EJECUCIÓN SECUENCIAL
# -------------------------------------------

print("\n=== EJECUCIÓN SECUENCIAL ===")

inicio = time.perf_counter()

# Primero se ejecuta una tarea.
tarea("Paco")

# Cuando termina, comienza la siguiente.
tarea("María")

fin = time.perf_counter()

print(f"Tiempo secuencial: {fin - inicio:.2f} segundos")


# -------------------------------------------
# SEGUNDA PARTE: EJECUCIÓN CON HILOS
# -------------------------------------------

print("\n=== EJECUCIÓN CON HILOS ===")

inicio = time.perf_counter()

# Creamos dos hilos.
hilo1 = threading.Thread(
    target=tarea,
    args=("Paco",)
)

hilo2 = threading.Thread(
    target=tarea,
    args=("María",)
)

# Iniciamos ambos hilos.
hilo1.start()
hilo2.start()

# Esperamos a que terminen los dos.
hilo1.join()
hilo2.join()

fin = time.perf_counter()

print(f"Tiempo con hilos: {fin - inicio:.2f} segundos")

print("\nPrograma finalizado.")
