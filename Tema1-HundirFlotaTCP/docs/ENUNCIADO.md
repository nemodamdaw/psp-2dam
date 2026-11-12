# PSPRO – 2.º DAM · Práctica: Hundir la flota con sockets TCP

**Tema 1 · Comunicación cliente-servidor**

## Objetivo

Crear un juego para **dos personas** que se comunican a través de una conexión **TCP**. El jugador 1 ejecuta `servidor.py` y el jugador 2 ejecuta `cliente.py`. Ambos juegan desde la consola de su ordenador.

No se utilizarán hilos, clases propias ni librerías externas. Solo Python y su biblioteca estándar.

## Reglas

- Cada participante tiene un tablero de **5 × 5**: columnas A–E y filas 1–5.
- El programa coloca **3 barcos de una casilla**, en posiciones diferentes y aleatorias.
- Empieza siempre el servidor.
- En cada turno se dispara a una casilla, por ejemplo `B3`.
- Se responde **AGUA** o **TOCADO**. El turno cambia siempre, incluso cuando se acierta.
- Una coordenada inválida o ya utilizada debe volver a pedirse; **no consume turno**.
- Gana quien encuentra los tres barcos del contrario.
- No se deben mostrar los barcos del contrincante.

### Leyenda de los tableros

| Carácter | Significado |
| --- | --- |
| `B` | Barco propio sin alcanzar |
| `.` | Agua propia todavía sin disparar |
| `X` | Barco tocado |
| `o` | Agua disparada |
| `?` | Casilla rival sin explorar |

## Archivos facilitados

```text
HundirFlotaTCP/
├── servidor.py
├── cliente.py
├── juego.py
└── docs/
    └── ENUNCIADO.md
```

En `juego.py` ya están implementadas las funciones de creación y visualización de tableros, validación de coordenadas y registro de disparos. **No modifiques sus cabeceras**. Completa los bloques marcados como `TODO`.

## Trabajo que hay que realizar

1. **TODO 1 – Lógica del disparo:** implementar `realizar_disparo` sin repetir disparos y actualizando el tablero propio.
2. **TODO 2 – Envío:** implementar `enviar_mensaje` con `sendall`, codificación UTF-8 y un salto de línea final.
3. **TODO 3 – Recepción:** implementar `recibir_mensaje` con `recv`, leyendo hasta `\n` y detectando desconexiones.
4. **TODO 4 – Partida:** implementar `jugar` con turnos alternos; quien dispara envía el disparo y espera el resultado, y quien recibe el disparo responde.
5. **TODO 5 – Servidor:** completar `bind`, `listen` y `accept` para aceptar un único cliente y empezar jugando.
6. **TODO 6 – Cliente:** completar `connect` para unirse al servidor y esperar el primer disparo.

## Protocolo de mensajes

Un mensaje es una línea de texto UTF-8 terminada en `\n`. No se intercambian tableros completos ni posiciones de barcos: cada jugador solo revela el resultado del disparo recibido.

**Ejemplo de turno:**

```text
Jugador que dispara -> DISPARO|B3
Jugador que recibe  -> RESULTADO|TOCADO|CONTINUA
```

El campo final de la respuesta es `CONTINUA` o `FIN`. Si es `FIN`, el último disparo ha ganado la partida y ambos programas deben terminar.

Otro ejemplo:

```text
DISPARO|A1
RESULTADO|AGUA|CONTINUA
```

**Atención:** TCP es un flujo de bytes. Una llamada a `recv(1024)` no garantiza recibir un mensaje completo y único. Para esta práctica, una solución sencilla es leer hasta `\n` mediante `recv(1)`.

## Ejecución

1. Abre dos terminales en la carpeta del proyecto.
2. En la primera terminal ejecuta `python servidor.py` (Windows también permite `py servidor.py`).
3. En la segunda terminal ejecuta `python cliente.py`.
4. El jugador 1 dispara primero. Ambos introducen las coordenadas cuando corresponda.

**Dos ordenadores:** deben estar en la misma red. En `cliente.py`, cambia `HOST = "127.0.0.1"` por la **IP local del ordenador servidor** (se puede consultar con `ipconfig` en Windows). Si aparece un aviso del cortafuegos, permite Python en redes privadas según las normas del centro. El puerto usado es **50505**; la red del centro puede impedir conexiones directas entre equipos.

## Pruebas obligatorias

- Ambos programas se conectan desde dos terminales o dos ordenadores.
- Una coordenada inválida, como `F2`, vuelve a solicitarse.
- Una casilla ya atacada vuelve a solicitarse.
- Se alternan los turnos sin bloqueo.
- El resultado coincide con el tablero del jugador atacado.
- Cuando un jugador alcanza los tres barcos, ambos ven quién ha ganado y finalizan.

## Entrega

Entregar una carpeta comprimida **`ApellidosNombre_HundirFlotaTCP.zip`** que contenga `servidor.py`, `cliente.py` y `juego.py`. Añadir un pequeño fichero `PRUEBAS.txt` que indique si se ha probado en el mismo ordenador o en dos equipos y qué comprobaciones se han realizado.

## Ampliación voluntaria

Permitir que los jugadores coloquen manualmente sus tres barcos antes de empezar, sin solaparlos y sin transmitir sus coordenadas al rival.
