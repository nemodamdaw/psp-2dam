# Ejemplo 10 - Multiprocessing Pool y map
from multiprocessing import Pool


def contar_divisores(numero):
    cantidad = 0
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            cantidad += 1
    return cantidad


if __name__ == "__main__":
    numeros = [10000, 12000, 15000, 18000]
    with Pool(processes=2) as grupo:
        resultados = grupo.map(contar_divisores, numeros)

    for numero, cantidad in zip(numeros, resultados):
        print(f"{numero} tiene {cantidad} divisores")
