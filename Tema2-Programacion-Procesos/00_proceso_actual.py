# TEMA 2 - PROGRAMACIÓN DE PROCESOS
# Ejemplo 00 - Identificar el proceso actual
# Ejecutar: python 00_proceso_actual.py

import os

print("Hola desde Python")
print("Mi PID:", os.getpid())
print("PID de mi proceso padre:", os.getppid())
