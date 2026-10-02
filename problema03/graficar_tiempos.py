import matplotlib.pyplot as plt

ARCHIVO_TRADICIONAL = "res_tradicional.txt"
ARCHIVO_ALTERNATIVO = "res_alternativo.txt"
GRAFICO_TRADICIONAL = "tradicional.png"
GRAFICO_ALTERNATIVO = "alternativo.png"
GRAFICO_COMPARACION = "comparacion.png"

def leer_resultados(nombre_archivo):
    resultados = []

    with open(nombre_archivo, "r") as archivo:

        for linea in archivo:
            partes = linea.split()

            if len(partes) != 4:
                continue
            
            if not partes[0].isdigit():
                continue

            n = int(partes[0])
            capacidad = int(partes[1])
            beneficio_total = int(partes[2])
            tiempo = float(partes[3])

            resultados.append((n, capacidad, beneficio_total, tiempo))

    return resultados

def calcular_factor_ajuste(valores_teoricos, tiempos):
    numerador = sum(valores_teoricos[i] * tiempos[i] for i in range(len(tiempos)))
    denominador = sum(valor ** 2 for valor in valores_teoricos)

    return numerador/denominador

def graficar_tradicional(resultados):
    tamanios = [resultado[0] for resultado in resultados]
    tiempos = [resultado[3] for resultado in resultados]
    valores_teoricos = [resultado[0] * resultado[1] for resultado in resultados]
    factor = calcular_factor_ajuste(valores_teoricos, tiempos)
    curva_teorica = [factor * valor for valor in valores_teoricos]

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanios,
        tiempos,
        marker="o",
        label="Tiempo real"
    )

    plt.plot(
        tamanios,
        curva_teorica,
        linestyle="--",
        label="Curva teórica ajustada O(nC)"
    )

    plt.xlabel("Cantidad de elementos (n)")
    plt.ylabel("Tiempo de ejecución (s)")

    plt.title(
        "Programación Dinámica - Mochila tradicional"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        GRAFICO_TRADICIONAL,
        dpi=150
    )

    plt.close()

def graficar_alternativo(resultados):
    tamanios = [resultado[0] for resultado in resultados]
    tiempos = [resultado[3] for resultado in resultados]
    valores_teoricos = [resultado[0] * resultado[2] for resultado in resultados]
    factor = calcular_factor_ajuste(valores_teoricos, tiempos)
    curva_teorica = [factor * valor for valor in valores_teoricos]

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanios,
        tiempos,
        marker="o",
        label="Tiempo real"
    )

    plt.plot(
        tamanios,
        curva_teorica,
        linestyle="--",
        label="Curva teórica ajustada O(nB)"
    )

    plt.xlabel("Cantidad de elementos (n)")
    plt.ylabel("Tiempo de ejecución (s)")

    plt.title(
        "Programación Dinámica - Mochila alternativa"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        GRAFICO_ALTERNATIVO,
        dpi=150
    )

    plt.close()

def graficar_comparacion(
    resultados_tradicional,
    resultados_alternativo
):
    tamanios = [resultado[0] for resultado in resultados_tradicional]
    tiempos_tradicional = [resultado[3] for resultado in resultados_tradicional]
    tiempos_alternativo = [resultado[3] for resultado in resultados_alternativo]

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanios,
        tiempos_tradicional,
        marker="o",
        label="Tradicional"
    )

    plt.plot(
        tamanios,
        tiempos_alternativo,
        marker="o",
        label="Alternativo"
    )

    plt.xlabel("Cantidad de elementos (n)")
    plt.ylabel("Tiempo de ejecución (s)")

    plt.title(
        "Programación Dinámica - Comparación de tiempos"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        GRAFICO_COMPARACION,
        dpi=150
    )

    plt.close()

def main():

    resultados_tradicional = leer_resultados(ARCHIVO_TRADICIONAL)
    resultados_alternativo = leer_resultados(ARCHIVO_ALTERNATIVO)
    graficar_tradicional(resultados_tradicional)
    graficar_alternativo(resultados_alternativo)
    graficar_comparacion(resultados_tradicional,resultados_alternativo)

if __name__ == "__main__":
    main()