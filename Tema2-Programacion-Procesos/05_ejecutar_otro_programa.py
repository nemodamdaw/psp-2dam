# Ejemplo 05 - Lanzar otro script Python y recoger su salida
import subprocess
import sys
from pathlib import Path


if __name__ == "__main__":
    ruta = Path(__file__).with_name("05_tarea_externa.py")
    resultado = subprocess.run(
        [sys.executable, str(ruta), "María"],
        capture_output=True,
        text=True,
        check=True
    )
    print("Salida del subproceso:")
    print(resultado.stdout.strip())
    print("Código de salida:", resultado.returncode)
