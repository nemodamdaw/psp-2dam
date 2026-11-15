# Ejemplo 07 - El hijo responde al padre mediante una tubería
import multiprocessing


def trabajador(conexion):
    dato = conexion.recv()
    conexion.send(f"He recibido: {dato.upper()}")
    conexion.close()


if __name__ == "__main__":
    padre, hijo = multiprocessing.Pipe()
    p = multiprocessing.Process(target=trabajador, args=(hijo,))
    p.start()
    hijo.close()
    padre.send("hola desde el padre")
    respuesta = padre.recv()
    print("Respuesta:", respuesta)
    padre.close()
    p.join()
