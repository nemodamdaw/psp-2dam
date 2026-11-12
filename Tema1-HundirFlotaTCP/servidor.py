"""Jugador 1: servidor TCP. Ejecutar primero."""

import socket
from juego import jugar

HOST = "0.0.0.0"   # Escucha en las interfaces de red del ordenador
PUERTO = 50505


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((HOST, PUERTO))
            servidor.listen(1)
            print(f"Jugador 1. Esperando rival en el puerto {PUERTO}...")

            conexion, direccion = servidor.accept()
            with conexion:
                print(f"Jugador 2 conectado desde {direccion[0]}")
                jugar(conexion, empieza=True)

    except (OSError, ConnectionError, ValueError) as error:
        print(f"Error de conexión o de partida: {error}")
    except (KeyboardInterrupt, EOFError):
        print("\nPartida interrumpida.")


if __name__ == "__main__":
    main()
