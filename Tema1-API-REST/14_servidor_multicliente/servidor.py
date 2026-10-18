
# TEMA 1 - SERVIDOR TCP MULTICLIENTE
# Ejemplo 14 - Servidor con un hilo por cliente
#
# Ejecutar desde Tema1-API-REST:
# ./.venv/bin/python 14_servidor_multicliente/servidor.py

import socket
import threading

HOST = "127.0.0.1"
PUERTO = 5003


# -------------------------------------------
# FUNCIÓN QUE ATIENDE A UN CLIENTE
# -------------------------------------------

def atender_cliente(conexion, direccion):

    print(f"Cliente conectado: {direccion}")

    with conexion:

        # Leemos mensajes terminados en \n.
        with conexion.makefile("r", encoding="utf-8") as lector:

            while True:

                # Esperamos un mensaje de ESTE cliente.
                linea = lector.readline()

                # Si se cierra la conexión, terminamos.
                if linea == "":
                    break

                mensaje = linea.rstrip("\r\n")

                print(f"{direccion}: {mensaje}")

                # El cliente quiere desconectarse.
                if mensaje.lower() == "salir":
                    conexion.sendall(b"ADIOS\n")
                    break

                # Respondemos al cliente en mayúsculas.
                respuesta = mensaje.upper()

                conexion.sendall(
                    (respuesta + "\n").encode("utf-8")
                )

    print(f"Cliente desconectado: {direccion}")


# -------------------------------------------
# PROGRAMA PRINCIPAL DEL SERVIDOR
# -------------------------------------------

with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
) as servidor:

    servidor.bind((HOST, PUERTO))
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PUERTO}")
    print("Esperando clientes...")

    try:

        while True:

            # Esperamos una nueva conexión.
            conexion, direccion = servidor.accept()

            # Creamos un hilo para el nuevo cliente.
            hilo = threading.Thread(
                target=atender_cliente,
                args=(conexion, direccion),
                daemon=True
            )

            # Iniciamos el hilo.
            hilo.start()

            print(f"Hilo iniciado para {direccion}")

    except KeyboardInterrupt:
        print("\nServidor detenido.")
