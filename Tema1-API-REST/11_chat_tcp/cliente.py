
# TEMA 1 - SOCKETS TCP
# Ejemplo 11 - CHAT TCP - CLIENTE
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 11_chat_tcp/cliente.py
#
# El cliente inicia la conversación.
# Cliente y servidor intercambian mensajes
# por turnos hasta que uno escriba "salir".

import socket

HOST = "127.0.0.1"
PUERTO = 5001

# Creamos el socket TCP del cliente.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

    # Nos conectamos al servidor.
    cliente.connect((HOST, PUERTO))

    print("Conectado al servidor.")
    print("Escribe 'salir' para terminar.")

    # Creamos un lector de texto sobre el socket.
    with cliente.makefile("r", encoding="utf-8") as lector:

        while True:

            # El cliente escribe un mensaje.
            mensaje = input("Cliente > ")

            # Enviamos el mensaje al servidor.
            cliente.sendall(
                (mensaje + "\n").encode("utf-8")
            )

            # Comprobamos si quiere terminar.
            if mensaje.lower() == "salir":
                print("Has terminado el chat.")
                break

            # Esperamos la respuesta del servidor.
            linea = lector.readline()

            # Comprobamos si se cerró la conexión.
            if linea == "":
                print("El servidor se ha desconectado.")
                break

            # Convertimos la línea recibida en mensaje.
            respuesta = linea.rstrip("\r\n")

            print(f"Servidor: {respuesta}")

            # El servidor solicita terminar.
            if respuesta.lower() == "salir":
                print("El servidor terminó el chat.")
                break

print("Cliente cerrado.")
