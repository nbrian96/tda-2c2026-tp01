import sys

def leer_mochila(nombre_archivo):
    elementos = []

    with open(nombre_archivo, "r") as archivo:
        capacidad = int(archivo.readline().strip())

        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                continue

            peso, beneficio = map(int, linea.split(","))

            elementos.append((peso, beneficio))

    return capacidad, elementos

def mochila_alternativo(elementos, capacidad):
    n = len(elementos)
    beneficio_total = sum(beneficio for peso, beneficio in elementos)
    infinito = float("inf")

    matriz_pesos = [[infinito for _ in range(beneficio_total + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        matriz_pesos[i][0] = 0

    for i in range(1, n + 1):
        peso, beneficio = elementos[i - 1]

        for beneficio_actual in range(1, beneficio_total + 1):

            if beneficio > beneficio_actual:
                matriz_pesos[i][beneficio_actual] = (matriz_pesos[i - 1][beneficio_actual])

            else:
                no_incluir = matriz_pesos[i - 1][beneficio_actual]
                incluir = (peso + matriz_pesos[i - 1][beneficio_actual - beneficio])
                matriz_pesos[i][beneficio_actual] = min(no_incluir, incluir)

    for beneficio_actual in range(beneficio_total, -1, -1):
        if matriz_pesos[n][beneficio_actual] <= capacidad:
            return beneficio_actual

    return 0

def main():
    if len(sys.argv) != 2:
        print("Uso:")
        print("python3 mochila_alternativo.py <archivo>")
        return

    nombre_archivo = sys.argv[1]

    capacidad, elementos = leer_mochila(nombre_archivo)

    beneficio_maximo = mochila_alternativo(elementos, capacidad)

    print("Beneficio máximo:", beneficio_maximo)

if __name__ == "__main__":
    main()