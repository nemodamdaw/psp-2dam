
# TEMA 1 - SOCKETS TCP
# Ejemplo 11 - CHAT TCP - SERVIDOR
#
# Para ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 11_chat_tcp/servidor.py
#
# El servidor atiende a un cliente y permite
# intercambiar varios mensajes por turnos.
# La conversación termina cuando uno escribe "salir".

import socket

HOST = "127.0.0.1"
PUERTO = 5001

# Creamos el socket TCP del servidor.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

    # Permite reutilizar el puerto al reiniciar el servidor.
    servidor.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    servidor.bind((HOST, PUERTO))
    servidor.listen(1)

    print(f"Servidor escuchando en {HOST}:{PUERTO}")
    print("Esperando cliente...")

    # Esperamos a que se conecte un cliente.
    conexion, direccion = servidor.accept()

    with conexion:
        print(f"Cliente conectado desde {direccion}")
        print("Escribe 'salir' para terminar.")

        # Creamos un lector de texto sobre el socket.
        with conexion.makefile("r", encoding="utf-8") as lector:

            # Mantenemos abierta la conversación.
            while True:

                # Esperamos un mensaje del cliente.
                linea = lector.readline()

                # Cadena vacía: el cliente cerró la conexión.
                if linea == "":
                    print("El cliente se ha desconectado.")
                    break

                # Quitamos el salto de línea final.
                mensaje = linea.rstrip("\r\n")

                print(f"Cliente: {mensaje}")

                # El cliente solicita terminar.
                if mensaje.lower() == "salir":
                    print("El cliente terminó el chat.")
                    break

                # El servidor escribe su respuesta.
                respuesta = input("Servidor > ")

                # Enviamos la respuesta con salto de línea.
                conexion.sendall(
                    (respuesta + "\n").encode("utf-8")
                )

                # El servidor solicita terminar.
                if respuesta.lower() == "salir":
                    print("Has terminado el chat.")
                    break

print("Servidor cerrado.")
