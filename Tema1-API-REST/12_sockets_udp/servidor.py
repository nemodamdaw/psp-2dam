
# TEMA 1 - SOCKETS UDP
# Ejemplo 12 - SERVIDOR UDP
#
# Ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 12_sockets_udp/servidor.py
#
# Recibe datagramas y envía respuestas.
# Termina cuando recibe el mensaje "salir".

import socket

HOST = "127.0.0.1"
PUERTO = 5002

# Creamos un socket UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:

    # Asociamos el socket con la dirección y el puerto.
    servidor.bind((HOST, PUERTO))

    print(f"Servidor UDP escuchando en {HOST}:{PUERTO}")
    print("Esperando mensajes...")

    while True:

        # Recibimos los datos y la dirección del cliente.
        datos, direccion = servidor.recvfrom(1024)

        # Convertimos los bytes a texto.
        mensaje = datos.decode("utf-8")

        print(f"Cliente {direccion}: {mensaje}")

        # Comprobamos si quiere terminar.
        if mensaje.strip().lower() == "salir":
            respuesta = "ADIOS"

            servidor.sendto(
                respuesta.encode("utf-8"),
                direccion
            )
            break

        # Preparamos la respuesta.
        if mensaje.upper() == "PING":
            respuesta = "PONG"
        else:
            respuesta = f"Recibido: {mensaje}"

        # Enviamos la respuesta al cliente.
        servidor.sendto(
            respuesta.encode("utf-8"),
            direccion
        )

        print(f"Respuesta enviada a {direccion}")

print("Servidor UDP cerrado.")
