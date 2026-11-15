# Archivo auxiliar utilizado por 05_ejecutar_otro_programa.py
import os
import sys

nombre = sys.argv[1] if len(sys.argv) > 1 else "sin nombre"
print(f"Hola {nombre}, soy el proceso {os.getpid()}")
