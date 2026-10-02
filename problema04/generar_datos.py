import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import crear_mochila

TAMANIOS = [10, 100, 1000, 10000, 50000, 100000, 150000]
SEMILLA = 42 


def generar_datasets(tamanios=TAMANIOS, semilla=SEMILLA):
    print("Generando datasets (semilla base = " + str(semilla) + ")...\n")
    for n in tamanios:
        random.seed(semilla + n)
        crear_mochila.crear_mochila(n)
        print("Dataset generado: mochila" + str(n) + ".txt")


if __name__ == "__main__":
    generar_datasets()