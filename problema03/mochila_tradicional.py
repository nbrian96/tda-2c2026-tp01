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

def mochila_tradicional(elementos, capacidad):
    n = len(elementos)

    matriz_optimos = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso, beneficio = elementos[i - 1]

        for c in range(1, capacidad + 1):

            if peso > c:
                matriz_optimos[i][c] = matriz_optimos[i - 1][c]

            else:
                no_incluir = matriz_optimos[i - 1][c]
                incluir = (beneficio + matriz_optimos[i - 1][c - peso])
                matriz_optimos[i][c] = max(no_incluir, incluir)

    return matriz_optimos[n][capacidad]

def main():
    if len(sys.argv) != 2:
        print("Uso:")
        print("python3 mochila_tradicional.py <archivo>")
        return

    nombre_archivo = sys.argv[1]

    capacidad, elementos = leer_mochila(nombre_archivo)

    beneficio_maximo = mochila_tradicional(elementos, capacidad)

    print("Beneficio máximo:", beneficio_maximo)

if __name__ == "__main__":
    main()