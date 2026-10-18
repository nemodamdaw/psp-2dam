
# TEMA 1 - CLIENTE TCP
# Ejemplo 14 - Cliente de servidor multicliente
#
# Ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 14_servidor_multicliente/cliente.py
#
# Ejecutaremos este mismo archivo varias veces.

import socket

HOST = "127.0.0.1"
PUERTO = 5003

nombre = input("¿Cómo te llamas? ")

with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
) as cliente:

    cliente.connect((HOST, PUERTO))

    print("Conectado al servidor.")
    print("Escribe 'salir' para terminar.")

    with cliente.makefile("r", encoding="utf-8") as lector:

        while True:

            mensaje = input(f"{nombre} > ")

            # Enviamos el mensaje terminado en \n.
            cliente.sendall(
                (mensaje + "\n").encode("utf-8")
            )

            # Esperamos la respuesta del servidor.
            respuesta = lector.readline()

            if respuesta == "":
                print("El servidor ha cerrado la conexión.")
                break

            print("Servidor:", respuesta.rstrip("\r\n"))

            if mensaje.lower() == "salir":
                break

print("Cliente finalizado.")
