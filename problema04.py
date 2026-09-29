from random import randint
import time
import matplotlib.pyplot as plt
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value
import crear_mochila


def leer_mochila(nombre_archivo):
    with open(nombre_archivo, "r") as f: 
        lineas = f.readlines()
    capacidad = int(lineas[0].strip())
    pesos = []
    valores = []
    for linea in lineas[1:]:
        partes = linea.strip().split(",")
        pesos.append(int(partes[0]))
        valores.append(int(partes[1]))
    return capacidad,pesos,valores

def construir_modelo(valores, pesos, capacidad):
    n = len(valores)
    modelo = LpProblem(name = "Mochila", sense=LpMaximize)
    X = [LpVariable("X_" + str(i), cat="Binary") for i in range(n)]
    modelo += lpSum(valores[i] * X[i] for i in range(n))
    modelo += lpSum(pesos[i] * X[i] for i in range(n)) <= capacidad
    return modelo,X

def resolver_mochila(valores, pesos, capacidad):
    modelo, X = construir_modelo(valores, pesos, capacidad)

    t_inicio = time.perf_counter()
    modelo.solve()
    t_fin = time.perf_counter()

    tiempo_solver = t_fin - t_inicio
    seleccionados = []
    valor_total = 0
    peso_total = 0
    for i in range(len(valores)):
        if value(X[i]) == 1:
            seleccionados.append(i)
            valor_total += valores[i]
            peso_total += pesos[i]

    return seleccionados, valor_total, peso_total, tiempo_solver


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

tamanios = [10, 50, 100, 200, 500, 1000, 2000, 5000]
repeticiones = 3
 
tiempos_promedio = []
 
print("Generando datasets y midiendo tiempos...\n")
 
for n in tamanios:
    crear_mochila.crear_mochila(n)
    capacidad, pesos, valores = leer_mochila("mochila" + str(n) + ".txt")
 
    tiempos = []
    for _ in range(repeticiones):
        _, _, _, t = resolver_mochila(valores, pesos, capacidad)
        tiempos.append(t)
 
    promedio = sum(tiempos) / repeticiones
    tiempos_promedio.append(promedio)
    print("n=" + str(n) + " | tiempo promedio solver: " + str(round(promedio, 6)) + "s")

with open("resultados_PL.txt", "w") as f:
    f.write("Resultados - Problema 4: Programacion Lineal\n")
    f.write("Tiempo medido: solo resolucion del solver \n")
    f.write("Repeticiones por instancia: " + str(repeticiones) + "\n")
    f.write("-" * 45 + "\n")
    f.write("{:<10} {:<15} {:<15}\n".format("n", "Capacidad W", "Tiempo (s)"))
    f.write("-" * 45 + "\n")
    for i in range(len(tamanios)):
        n = tamanios[i]
        f.write("{:<10} {:<15} {:<15}\n".format(
            n,
            n * 50,
            round(tiempos_promedio[i], 6)
        ))
 
print("\nResultados guardados en resultados_PL.txt")

k = tiempos_promedio[0] / (tamanios[0] ** 3)
curva_teorica = [k * (n ** 3) for n in tamanios]
 
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_promedio, marker="o", label="Tiempo real", color="steelblue", linewidth=2)
plt.plot(tamanios, curva_teorica, marker="s", label="Curva teórica O(n³)", color="orange", linewidth=2, linestyle="--")
plt.xlabel("n (cantidad de elementos)")
plt.ylabel("Tiempo (segundos)")
plt.title("Problema 4 - Programación Lineal: Tiempo del solver vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("tiempos_PL.png", dpi=150)
plt.show()
 
print("Gráfico guardado en tiempos_PL.png")