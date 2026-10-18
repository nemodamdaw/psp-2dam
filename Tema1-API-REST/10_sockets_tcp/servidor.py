
# TEMA 1 - SOCKETS TCP
# Ejemplo 09 - SERVIDOR
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 10_sockets_tcp/servidor.py
#
# El servidor espera un cliente.
# Recibe un mensaje y devuelve una respuesta.

import socket

# Dirección IP y puerto del servidor.
HOST = "127.0.0.1"
PUERTO = 5001

# Creamos un socket TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

    # Asociamos el socket con una dirección y puerto.
    servidor.bind((HOST, PUERTO))

    # El servidor comienza a escuchar conexiones.
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PUERTO}")
    print("Esperando a que se conecte un cliente...")

    # Esperamos hasta que un cliente se conecte.
    conexion, direccion = servidor.accept()

    with conexion:

        print(f"Cliente conectado desde {direccion}")

        # Recibimos hasta 1024 bytes.
        datos = conexion.recv(1024)

        # Convertimos los bytes recibidos en texto.
        mensaje = datos.decode("utf-8")

        print(f"Mensaje recibido: {mensaje}")

        # Preparamos la respuesta del servidor.
        if mensaje.upper() == "PING":
            respuesta = "PONG"
        else:
            respuesta = f"Has enviado: {mensaje}"

        # Enviamos la respuesta al cliente.
        conexion.sendall(respuesta.encode("utf-8"))

        print(f"Respuesta enviada: {respuesta}")

# Al salir de los bloques with se cierran los sockets.
print("Servidor finalizado.")
