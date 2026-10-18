
# TEMA 1 - SOCKETS TCP
# Ejemplo 09 - CLIENTE
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 10_sockets_tcp/cliente.py
#
# El cliente se conecta al servidor,
# envía un mensaje y recibe la respuesta.

import socket

# Dirección IP y puerto del servidor.
HOST = "127.0.0.1"
PUERTO = 5001

# Creamos un socket TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

    # Nos conectamos al servidor.
    cliente.connect((HOST, PUERTO))

    print("Conectado al servidor.")

    # Mensaje que vamos a enviar.
    print("escribe un mensaje para enviar al servidor:")
    mensaje = input()

    # Convertimos el texto en bytes y lo enviamos.
    cliente.sendall(mensaje.encode("utf-8"))

    print(f"Mensaje enviado: {mensaje}")

    # Esperamos la respuesta del servidor.
    datos = cliente.recv(1024)

    # Convertimos los bytes recibidos en texto.
    respuesta = datos.decode("utf-8")

    print(f"Respuesta recibida: {respuesta}")

# El socket del cliente se cierra automáticamente.
print("Cliente finalizado.")
