"""Jugador 2: cliente TCP. Cambiar HOST para jugar en otro equipo."""

import socket
from juego import jugar

HOST = "127.0.0.1"  # Sustituir por la IP del servidor si está en otro PC
PUERTO = 50505


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PUERTO))
            print(f"Jugador 2. Conectado a {HOST}:{PUERTO}")
            jugar(cliente, empieza=False)

    except (OSError, ConnectionError, ValueError) as error:
        print(f"Error de conexión o de partida: {error}")
    except (KeyboardInterrupt, EOFError):
        print("\nPartida interrumpida.")


if __name__ == "__main__":
    main()
