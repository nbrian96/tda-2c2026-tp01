import time
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value, PULP_CBC_CMD


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
    modelo.solve(PULP_CBC_CMD(msg=0))
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
