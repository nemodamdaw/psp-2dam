"""Lógica de Hundir la flota y protocolo de mensajes TCP.

Dos jugadores, tres barcos de una casilla y un disparo por turno.
No se utilizan hilos ni clases definidas por el alumnado.
"""

import random

TAMANO = 5
NUM_BARCOS = 3
COLUMNAS = "ABCDE"


def crear_tablero(vacio=False):
    """Devuelve una matriz 5x5. Si vacio es False, coloca tres barcos."""
    simbolo = "?" if vacio else "."
    tablero = [[simbolo for _ in range(TAMANO)] for _ in range(TAMANO)]

    if not vacio:
        posiciones = random.sample(range(TAMANO * TAMANO), NUM_BARCOS)
        for posicion in posiciones:
            fila = posicion // TAMANO
            columna = posicion % TAMANO
            tablero[fila][columna] = "B"

    return tablero


def mostrar_tablero(tablero):
    """Imprime filas 1-5 y columnas A-E."""
    print("    " + " ".join(COLUMNAS))
    for numero, fila in enumerate(tablero, start=1):
        print(f"{numero}   " + " ".join(fila))


def coordenada_a_indices(coordenada):
    """Convierte 'B3' en (2, 1); devuelve None si no es válida."""
    indices = None
    coordenada = coordenada.strip().upper()
    if len(coordenada) == 2:
        letra = coordenada[0]
        numero = coordenada[1]
        if letra in COLUMNAS and numero in "12345":
            indices = (int(numero) - 1, COLUMNAS.index(letra))
    return indices


def realizar_disparo(tablero, coordenada):
    """Actualiza el tablero propio y devuelve AGUA, TOCADO o REPETIDO."""
    indices = coordenada_a_indices(coordenada)
    if indices is None:
        raise ValueError("Coordenada incorrecta")

    fila, columna = indices
    casilla = tablero[fila][columna]
    resultado = "REPETIDO"

    if casilla == "B":
        tablero[fila][columna] = "X"
        resultado = "TOCADO"
    elif casilla == ".":
        tablero[fila][columna] = "o"
        resultado = "AGUA"

    return resultado


def barcos_restantes(tablero):
    """Cuenta las casillas con barcos todavía no alcanzados."""
    cantidad = 0
    for fila in tablero:
        for casilla in fila:
            if casilla == "B":
                cantidad += 1
    return cantidad


def pedir_disparo(disparos):
    """Solicita una coordenada válida que aún no se haya utilizado."""
    coordenada = ""
    correcto = False

    while not correcto:
        coordenada = input("Dispara (por ejemplo, B3): ").strip().upper()
        indices = coordenada_a_indices(coordenada)

        if indices is None:
            print("Coordenada no válida. Utiliza A1, B3, E5, etc.")
        else:
            fila, columna = indices
            if disparos[fila][columna] != "?":
                print("Ya has disparado a esa casilla.")
            else:
                correcto = True

    return coordenada


def actualizar_disparos(disparos, coordenada, resultado):
    """Registra el resultado en el tablero de disparos propios."""
    fila, columna = coordenada_a_indices(coordenada)
    if resultado == "TOCADO":
        disparos[fila][columna] = "X"
    elif resultado == "AGUA":
        disparos[fila][columna] = "o"
    else:
        raise ValueError("Resultado de disparo desconocido")


def enviar_mensaje(conexion, mensaje):
    """Envía un mensaje textual terminado en salto de línea."""
    datos = (mensaje + "\n").encode("utf-8")
    conexion.sendall(datos)


def recibir_mensaje(conexion):
    """Lee hasta '\n'. recv(1) se usa por claridad con mensajes pequeños.

    TCP transmite un flujo de bytes: recv(1024) NO garantiza recibir
    exactamente un mensaje. El separador impide juntar o cortar mensajes.
    """
    datos = bytearray()
    terminado = False

    while not terminado:
        fragmento = conexion.recv(1)
        if not fragmento:
            raise ConnectionError("El otro jugador se ha desconectado")
        if fragmento == b"\n":
            terminado = True
        else:
            datos.extend(fragmento)
            if len(datos) > 64:
                raise ValueError("Mensaje demasiado largo")

    return datos.decode("utf-8")


def jugar(conexion, empieza):
    """Bucle común a servidor y cliente. empieza=True para el servidor.

    En el propio turno: enviar DISPARO|B3, recibir RESULTADO|AGUA|CONTINUA.
    En el turno rival: recibir DISPARO|B3, enviar RESULTADO|...|... .
    FIN identifica el último disparo que gana la partida.
    """
    tablero_propio = crear_tablero()
    tablero_disparos = crear_tablero(vacio=True)
    mi_turno = empieza
    partida_terminada = False

    print("\n¡Partida iniciada!")
    print("Leyenda: B=barco, X=tocado, o=agua, ?=desconocido")
    print("\nTu tablero:")
    mostrar_tablero(tablero_propio)

    while not partida_terminada:
        if mi_turno:
            print("\n--- TU TURNO ---")
            print("Tus disparos hasta ahora:")
            mostrar_tablero(tablero_disparos)

            coordenada = pedir_disparo(tablero_disparos)
            enviar_mensaje(conexion, "DISPARO|" + coordenada)

            mensaje = recibir_mensaje(conexion)
            partes = mensaje.split("|")
            if (len(partes) != 3 or partes[0] != "RESULTADO"
                    or partes[1] not in ("AGUA", "TOCADO")
                    or partes[2] not in ("FIN", "CONTINUA")):
                raise ValueError("Respuesta inesperada: " + mensaje)

            resultado = partes[1]
            actualizar_disparos(tablero_disparos, coordenada, resultado)
            print(f"Tu disparo a {coordenada}: {resultado}")

            if partes[2] == "FIN":
                print("\n¡HAS GANADO! Has encontrado todos los barcos rivales.")
                partida_terminada = True
            else:
                mi_turno = False

        else:
            print("\n--- TURNO DEL RIVAL ---")
            print("Esperando su disparo...")
            mensaje = recibir_mensaje(conexion)
            partes = mensaje.split("|")
            if len(partes) != 2 or partes[0] != "DISPARO":
                raise ValueError("Mensaje inesperado: " + mensaje)

            coordenada = partes[1]
            resultado = realizar_disparo(tablero_propio, coordenada)
            if resultado == "REPETIDO":
                raise ValueError("El rival ha repetido un disparo")

            estado = "CONTINUA"
            if barcos_restantes(tablero_propio) == 0:
                estado = "FIN"

            enviar_mensaje(conexion, f"RESULTADO|{resultado}|{estado}")
            print(f"El rival ha disparado a {coordenada}: {resultado}")
            print("Tu tablero:")
            mostrar_tablero(tablero_propio)

            if estado == "FIN":
                print("\nHAS PERDIDO. El rival ha encontrado todos tus barcos.")
                partida_terminada = True
            else:
                mi_turno = True
