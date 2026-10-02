import math
import matplotlib.pyplot as plt

from generar_datos import TAMANIOS
from problema04 import leer_mochila, resolver_mochila

REPETICIONES = 3
ARCHIVO_TXT = "resultados_PL.txt"
ARCHIVO_PNG = "tiempos_PL.png"


def medir_tiempos(tamanios=TAMANIOS, repeticiones=REPETICIONES):
    """Resuelve cada instancia varias veces y devuelve capacidades y tiempos promedio."""
    capacidades = []
    tiempos_promedio = []

    print("Midiendo tiempos del solver...\n")
    for n in tamanios:
        capacidad, pesos, valores = leer_mochila("mochila" + str(n) + ".txt")

        tiempos = []
        for _ in range(repeticiones):
            _, _, _, t = resolver_mochila(valores, pesos, capacidad)
            tiempos.append(t)

        promedio = sum(tiempos) / repeticiones
        capacidades.append(capacidad)
        tiempos_promedio.append(promedio)
        print("n=" + str(n) + " | tiempo promedio solver: " + str(round(promedio, 6)) + "s")

    return capacidades, tiempos_promedio


def guardar_resultados(tamanios, capacidades, tiempos_promedio, repeticiones=REPETICIONES):
    with open(ARCHIVO_TXT, "w") as f:
        f.write("Resultados - Problema 4: Programacion Lineal\n")
        f.write("Tiempo medido: solo resolucion del solver\n")
        f.write("Repeticiones por instancia: " + str(repeticiones) + "\n")
        f.write("-" * 45 + "\n")
        f.write("{:<10} {:<15} {:<15}\n".format("n", "Capacidad W", "Tiempo (s)"))
        f.write("-" * 45 + "\n")
        for i in range(len(tamanios)):
            f.write("{:<10} {:<15} {:<15}\n".format(
                tamanios[i], capacidades[i], round(tiempos_promedio[i], 6)
            ))
    print("\nResultados guardados en " + ARCHIVO_TXT)


def graficar(tamanios, tiempos_promedio):
    n0 = tamanios[0]
    log_t0 = math.log10(tiempos_promedio[0])
    log_teorica = [log_t0 + (n - n0) * math.log10(2) for n in tamanios]
    log_real = [math.log10(t) for t in tiempos_promedio]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, log_real, marker="o", label="Tiempo real (solver)",
             color="steelblue", linewidth=2)
    plt.plot(tamanios, log_teorica, marker="s", label="Curva teórica O(2^n)",
             color="orange", linewidth=2, linestyle="--")
    plt.xlabel("n (cantidad de elementos)")
    plt.ylabel("log10( tiempo en segundos )")
    plt.title("Problema 4 - Programación Lineal: Tiempo del solver vs n")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(ARCHIVO_PNG, dpi=150)
    plt.show()

    print("Gráfico guardado en " + ARCHIVO_PNG)


if __name__ == "__main__":
    capacidades, tiempos_promedio = medir_tiempos()
    guardar_resultados(TAMANIOS, capacidades, tiempos_promedio)
    graficar(TAMANIOS, tiempos_promedio)