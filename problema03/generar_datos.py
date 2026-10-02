import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import crear_mochila

TAMANIOS = [ 10, 20, 50, 100, 200, 300, 400, 500, 600, 800, 1000 ]
# TAMANIOS = [ 10, 20, 50 , 100 ]
SEMILLA = 2026

def generar_datasets(tamanios=TAMANIOS, semilla=SEMILLA):

    for n in tamanios:
        semilla_actual = semilla + n
        random.seed(semilla_actual)
        crear_mochila.crear_mochila(n)

if __name__ == "__main__":
    generar_datasets()