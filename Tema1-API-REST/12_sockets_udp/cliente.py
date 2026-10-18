
# TEMA 1 - SOCKETS UDP
# Ejemplo 12 - CLIENTE UDP
#
# Ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 12_sockets_udp/cliente.py
#
# Envía mensajes al servidor y muestra sus respuestas.

import socket

HOST = "127.0.0.1"
PUERTO = 5002

# Creamos un socket UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:

    # Esperamos como máximo 3 segundos una respuesta.
    cliente.settimeout(3)

    print("Cliente UDP preparado.")
    print("Escribe 'salir' para terminar.")

    while True:

        mensaje = input("Cliente > ")

        # Enviamos un datagrama al servidor.
        cliente.sendto(
            mensaje.encode("utf-8"),
            (HOST, PUERTO)
        )

        print("Mensaje enviado.")

        # Intentamos recibir la respuesta.
        try:
            datos, direccion = cliente.recvfrom(1024)

            respuesta = datos.decode("utf-8")

            print(f"Servidor {direccion}: {respuesta}")

        except socket.timeout:
            print("No se ha recibido respuesta en 3 segundos.")

        # Terminamos si hemos enviado "salir".
        if mensaje.strip().lower() == "salir":
            break

print("Cliente UDP cerrado.")
