import time

from generar_datos import TAMANIOS
from mochila_tradicional import leer_mochila, mochila_tradicional
from mochila_alternativo import mochila_alternativo

REPETICIONES = 3

ARCHIVO_TRADICIONAL = "res_tradicional.txt"
ARCHIVO_ALTERNATIVO = "res_alternativo.txt"

def medir_tiempo(algoritmo, elementos, capacidad):
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(elementos, capacidad)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / REPETICIONES

def guardar_resultados(nombre_archivo, nombre_algoritmo, resultados):
    with open(nombre_archivo, "w") as archivo:

        archivo.write("Resultados - Problema 3: Programación Dinámica\n")

        archivo.write("Algoritmo: " + nombre_algoritmo + "\n")

        archivo.write("Repeticiones por instancia: " + str(REPETICIONES) + "\n")

        archivo.write("Tiempo medido: solamente ejecución del algoritmo\n")

        archivo.write("-" * 75 + "\n")

        archivo.write(
            "{:<10} {:<15} {:<20} {:<20}\n".format(
                "n",
                "Capacidad",
                "Beneficio Total",
                "Tiempo Promedio (s)"
            )
        )

        archivo.write("-" * 75 + "\n")

        for n, capacidad, beneficio_total, tiempo in resultados:
            archivo.write(
                "{:<10} {:<15} {:<20} {:<20.6f}\n".format(
                    n,
                    capacidad,
                    beneficio_total,
                    tiempo
                )
            )

def main():
    resultados_tradicional = []
    resultados_alternativo = []

    for n in TAMANIOS:
        nombre_archivo = "mochila" + str(n) + ".txt"

        capacidad, elementos = leer_mochila(nombre_archivo)

        beneficio_total = sum(beneficio for peso, beneficio in elementos)

        tiempo_tradicional = medir_tiempo(mochila_tradicional, elementos, capacidad)

        tiempo_alternativo = medir_tiempo(mochila_alternativo, elementos, capacidad)

        resultados_tradicional.append((n, capacidad, beneficio_total, tiempo_tradicional))

        resultados_alternativo.append((n, capacidad, beneficio_total, tiempo_alternativo))

    guardar_resultados(ARCHIVO_TRADICIONAL, "Mochila tradicional", resultados_tradicional)
    guardar_resultados(ARCHIVO_ALTERNATIVO, "Mochila alternativo", resultados_alternativo)

if __name__ == "__main__":
    main()