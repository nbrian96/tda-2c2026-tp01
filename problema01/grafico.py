import csv
import os
import random
import time

import matplotlib.pyplot as plt

from codigo import Elemento, Mochila, backtracking, fuerzaBruta

TAMANIOS_FUERZA_BRUTA = list(range(2, 29, 2))
TAMANIOS_BACKTRACKING = list(range(2, 41, 2))
REPETICIONES = 3
SEMILLA = 42
TIEMPO_POR_OPERACION = 1e-8  # segundos que se asume que tarda cada operacion elemental

# Para n >= 30 (solo backtracking) se generaron 7 instancias por tamanio con semillas
# SEMILLA + n + 1000*k (k = 0..6) y se eligio la de tiempo mediano. En n = 30 y n = 40
# la mediana fue la semilla por defecto (k = 0), por eso no aparecen aca.
SEMILLAS_ELEGIDAS = {32: 3074, 34: 1076, 36: 3078, 38: 5080}

COLOR_FUERZA_BRUTA = "#2a78d6"
COLOR_BACKTRACKING = "#eb6834"
COLOR_TEORICO = "#6b6a63"


def crearElementos(n):
    # Misma distribucion que crear_mochila.py: pesos 1-200, beneficios 1-1000, capacidad n*50
    generador = random.Random(SEMILLAS_ELEGIDAS.get(n, SEMILLA + n))
    elementos = [Elemento(generador.randint(1, 200), generador.randint(1, 1000)) for _ in range(n)]
    return n * 50, elementos


def medirTiempo(algoritmo, pesoMochila, elementos):
    # Me quedo con el minimo de varias corridas para reducir el ruido del sistema
    mejorTiempo = float("inf")
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(Mochila(pesoMochila), elementos, Mochila(pesoMochila))
        mejorTiempo = min(mejorTiempo, time.perf_counter() - inicio)
    return mejorTiempo


def complejidadTeorica(n):
    return n * 2 ** n


def tiempoTeorico(n):
    # Tiempo simulado: cantidad de operaciones teoricas por el tiempo asumido de cada operacion
    return complejidadTeorica(n) * TIEMPO_POR_OPERACION


def graficarAjuste(eje, tamanios, tiempos, color, titulo, limitarAlMedido=False):
    curvaTeorica = [tiempoTeorico(n) for n in tamanios]

    eje.plot(tamanios, curvaTeorica, color=COLOR_TEORICO, linewidth=2, linestyle="--",
             label=r"Teórico: $O(n \cdot 2^n)$")
    eje.plot(tamanios, tiempos, color=color, linewidth=2, marker="o", markersize=7, label="Medido")
    if limitarAlMedido:
        # La curva teorica sigue en la misma escala pero sale por arriba del grafico
        tope = max(tiempos) * 1.15
        eje.set_ylim(-tope * 0.04, tope)
    eje.set_title(titulo)
    eje.set_xlabel("Cantidad de elementos (n)")
    eje.set_ylabel("Tiempo (s)")
    eje.legend(loc="upper left")


def guardarResultados(ruta, tiemposFuerzaBruta, tiemposBacktracking):
    # Fuerza bruta se mide en menos tamanios, esos casilleros quedan vacios
    porTamanioFuerzaBruta = dict(zip(TAMANIOS_FUERZA_BRUTA, tiemposFuerzaBruta))
    with open(ruta, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "fuerza_bruta_s", "backtracking_s"])
        for n, tiempoBacktracking in zip(TAMANIOS_BACKTRACKING, tiemposBacktracking):
            escritor.writerow([n, porTamanioFuerzaBruta.get(n, ""), tiempoBacktracking])


if __name__ == "__main__":
    directorio = os.path.dirname(os.path.abspath(__file__))
    tiemposFuerzaBruta = []
    tiemposBacktracking = []

    for n in TAMANIOS_FUERZA_BRUTA:
        pesoMochila, elementos = crearElementos(n)
        tiemposFuerzaBruta.append(medirTiempo(fuerzaBruta, pesoMochila, elementos))
        print(f"Fuerza bruta  | n = {n:2d} | {tiemposFuerzaBruta[-1]:.6f} s", flush=True)

    for n in TAMANIOS_BACKTRACKING:
        pesoMochila, elementos = crearElementos(n)
        tiemposBacktracking.append(medirTiempo(backtracking, pesoMochila, elementos))
        print(f"Backtracking  | n = {n:2d} | {tiemposBacktracking[-1]:.6f} s", flush=True)

    guardarResultados(os.path.join(directorio, "tiempos.csv"), tiemposFuerzaBruta, tiemposBacktracking)

    figura, (ejeFuerzaBruta, ejeBacktracking, ejeComparacion) = plt.subplots(1, 3, figsize=(18, 5.5))

    graficarAjuste(ejeFuerzaBruta, TAMANIOS_FUERZA_BRUTA, tiemposFuerzaBruta, COLOR_FUERZA_BRUTA, "Fuerza bruta")
    graficarAjuste(ejeBacktracking, TAMANIOS_BACKTRACKING, tiemposBacktracking, COLOR_BACKTRACKING, "Backtracking",
                   limitarAlMedido=True)

    ejeComparacion.plot(TAMANIOS_FUERZA_BRUTA, tiemposFuerzaBruta, color=COLOR_FUERZA_BRUTA, linewidth=2, marker="o", markersize=7, label="Fuerza bruta")
    ejeComparacion.plot(TAMANIOS_BACKTRACKING, tiemposBacktracking, color=COLOR_BACKTRACKING, linewidth=2, marker="o", markersize=7, label="Backtracking")
    ejeComparacion.set_title("Comparación")
    ejeComparacion.set_xlabel("Cantidad de elementos (n)")
    ejeComparacion.set_ylabel("Tiempo (s)")
    ejeComparacion.legend()

    for eje in (ejeFuerzaBruta, ejeBacktracking, ejeComparacion):
        eje.grid(True, color="#e0e0e0", linewidth=0.8)
        eje.set_axisbelow(True)
        for borde in ("top", "right"):
            eje.spines[borde].set_visible(False)

    figura.tight_layout()
    figura.savefig(os.path.join(directorio, "grafico.png"), dpi=150)
    plt.show()
