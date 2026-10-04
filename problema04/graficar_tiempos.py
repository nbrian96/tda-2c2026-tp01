import matplotlib.pyplot as plt
import numpy as np

from generar_datos import TAMANIOS
from problema04 import leer_mochila, resolver_mochila

REPETICIONES = 3
ARCHIVO_TXT = "resultados_PL.txt"
ARCHIVO_PNG = "tiempos_PL.png"

# Hasta qué n se dibuja la curva exponencial en escala lineal (panel izquierdo)
N_EXP_MAX = 30
# Hasta qué n se dibuja la cota exponencial en el panel derecho (más allá no es representable)
N_COTA_MAX = 60


def medir_tiempos(tamanios=TAMANIOS, repeticiones=REPETICIONES):
    """Resuelve cada instancia varias veces y devuelve capacidades y tiempos promedio."""
    capacidades = []
    tiempos_promedio = []

    print("Midiendo tiempos del solver...\n")

    # Corrida de calentamiento: la primera llamada a CBC es mas lenta (carga del solver)
    # y distorsionaria el tiempo de la primera instancia.
    resolver_mochila([1], [1], 1)

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
    n0, t0 = tamanios[0], tiempos_promedio[0]

    figura, (ejeLineal, ejeLog) = plt.subplots(1, 2, figsize=(15, 6))

    # Panel izquierdo: curva exponencial en escala lineal, solo para n chico
    n_exp = list(range(n0, N_EXP_MAX + 1))
    t_exp = [t0 * 2 ** (n - n0) for n in n_exp]
    ejeLineal.plot(n_exp, t_exp, color="orange", linewidth=2, linestyle="--",
                   label="Curva teórica O(2^n) (anclada en n=" + str(n0) + ")")
    medidos = [(n, t) for n, t in zip(tamanios, tiempos_promedio) if n <= N_EXP_MAX]
    ejeLineal.plot([m[0] for m in medidos], [m[1] for m in medidos], marker="o",
                   color="steelblue", linewidth=2, label="Tiempo real (solver)")
    ejeLineal.set_ylim(-0.03 * t_exp[-1], t_exp[-1])
    ejeLineal.set_title("Escala lineal, n ≤ " + str(N_EXP_MAX))
    ejeLineal.set_xlabel("n (cantidad de elementos)")
    ejeLineal.set_ylabel("Tiempo (s)")

    # Panel derecho: todos los tamaños en escala log-log, con ajuste empírico t = a * n^b
    b, log_a = np.polyfit(np.log10(tamanios), np.log10(tiempos_promedio), 1)
    n_ajuste = np.logspace(np.log10(tamanios[0]), np.log10(tamanios[-1]), 100)
    t_ajuste = (10 ** log_a) * n_ajuste ** b
    n_cota = list(range(n0, N_COTA_MAX + 1))
    t_cota = [t0 * 2 ** (n - n0) for n in n_cota]

    ejeLog.plot(tamanios, tiempos_promedio, marker="o", color="steelblue", linewidth=2,
                label="Tiempo real (solver)")
    ejeLog.plot(n_ajuste, t_ajuste, color="green", linewidth=2, linestyle=":",
                label="Ajuste empírico ~ n^" + str(round(b, 2)))
    ejeLog.plot(n_cota, t_cota, color="orange", linewidth=2, linestyle="--",
                label="Cota teórica O(2^n)")
    ejeLog.set_xscale("log")
    ejeLog.set_yscale("log")
    ejeLog.set_ylim(min(tiempos_promedio) / 2, max(tiempos_promedio) * 10)
    ejeLog.set_title("Escala logarítmica, todos los tamaños")
    ejeLog.set_xlabel("n (cantidad de elementos, escala log)")
    ejeLog.set_ylabel("Tiempo (s, escala log)")

    for eje in (ejeLineal, ejeLog):
        eje.legend()
        eje.grid(True, which="both")

    figura.suptitle("Problema 4 - Programación Lineal: Tiempo del solver vs n")
    figura.tight_layout()
    figura.savefig(ARCHIVO_PNG, dpi=150)
    plt.show()

    print("Gráfico guardado en " + ARCHIVO_PNG)


if __name__ == "__main__":
    capacidades, tiempos_promedio = medir_tiempos()
    guardar_resultados(TAMANIOS, capacidades, tiempos_promedio)
    graficar(TAMANIOS, tiempos_promedio)