import os


class Elemento:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor


class Mochila:
    def __init__(self, peso):
        self.peso = peso
        self.pesoDisponible = peso
        self.valorActual = 0
        self.itemsDentro = []

    def agregarElemento(self, elemento):
        self.itemsDentro.append(elemento)
        self.pesoDisponible -= elemento.peso
        self.valorActual += elemento.valor

    def quitarElemento(self):
        elemento = self.itemsDentro.pop()
        self.pesoDisponible += elemento.peso
        self.valorActual -= elemento.valor
        return elemento

    def puedeAgregarElemento(self, elemento):
        return self.pesoDisponible >= elemento.peso

    def copiar(self):
        copia = Mochila(self.peso)
        copia.pesoDisponible = self.pesoDisponible
        copia.valorActual = self.valorActual
        copia.itemsDentro = list(self.itemsDentro)
        return copia


def leerArchivo(ruta):
    with open(ruta) as archivo:
        pesoMochila = int(archivo.readline())
        elementos = []
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            peso, valor = linea.split(",")
            elementos.append(Elemento(int(peso), int(valor)))
    return pesoMochila, elementos

def fuerzaBruta(mochila, elementos, mejorResultado):
    resultadoADevolver = mejorResultado
    if mochila.valorActual > resultadoADevolver.valorActual:
        resultadoADevolver = mochila.copiar()
        
    elementosAProbar = list(elementos)
    for elemento in elementos:
        elementoPivote = elementosAProbar.pop(0)
        if mochila.puedeAgregarElemento(elementoPivote):
            mochila.agregarElemento(elementoPivote)
            copiaMochila = mochila.copiar()
            copiaListaElementosSinPivote = list(elementosAProbar)
            resultadoRecurrencia = fuerzaBruta(copiaMochila, copiaListaElementosSinPivote, resultadoADevolver)
            if resultadoRecurrencia.valorActual > resultadoADevolver.valorActual:
                resultadoADevolver = resultadoRecurrencia
            mochila.quitarElemento()
        else: continue

    return resultadoADevolver

def cotaSuperior(mochila, elementos):
    # Valor optimista: lo que ya tengo + todo lo que todavia entraria individualmente
    cota = mochila.valorActual
    for elemento in elementos:
        if mochila.puedeAgregarElemento(elemento):
            cota += elemento.valor
    return cota

def backtracking(mochila, elementos, mejorResultado):
    resultadoADevolver = mejorResultado
    if mochila.valorActual > resultadoADevolver.valorActual:
        resultadoADevolver = mochila.copiar()

    # Poda: si ni en el mejor caso supero al mejor resultado, no sigo explorando esta rama
    if cotaSuperior(mochila, elementos) <= resultadoADevolver.valorActual:
        return resultadoADevolver

    elementosAProbar = list(elementos)
    for elemento in elementos:
        elementoPivote = elementosAProbar.pop(0)
        if mochila.puedeAgregarElemento(elementoPivote):
            mochila.agregarElemento(elementoPivote)
            resultadoRecurrencia = backtracking(mochila, elementosAProbar, resultadoADevolver)
            if resultadoRecurrencia.valorActual > resultadoADevolver.valorActual:
                resultadoADevolver = resultadoRecurrencia
            mochila.quitarElemento()
            # Poda: con los elementos que quedan ya no puedo superar al mejor
            if cotaSuperior(mochila, elementosAProbar) <= resultadoADevolver.valorActual:
                break

    return resultadoADevolver

if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Mochilas", "mochila5.txt")
    pesoMochila, elementos = leerArchivo(ruta)

    print("Peso de la mochila:", pesoMochila)
    print("Cantidad de elementos:", len(elementos))

    for elemento in elementos[:5]:
        print("Peso:", elemento.peso, "- Valor:", elemento.valor)

    print("-------------------------------------------------------")
    mochila = Mochila(pesoMochila)
    resultadoObtenido = fuerzaBruta(mochila.copiar(), elementos, mochila.copiar())
    print("Peso disponible resultado:", resultadoObtenido.pesoDisponible, "- Valor conseguido:", resultadoObtenido.valorActual)
    print("Elementos colocados:")
    for elemento in resultadoObtenido.itemsDentro:
        print("Peso:", elemento.peso, "- Valor:", elemento.valor)

    print("-------------------------------------------------------")
    resultadoBacktracking = backtracking(mochila.copiar(), elementos, mochila.copiar())
    print("Backtracking - Peso disponible resultado:", resultadoBacktracking.pesoDisponible, "- Valor conseguido:", resultadoBacktracking.valorActual)
    print("Elementos colocados:")
    for elemento in resultadoBacktracking.itemsDentro:
        print("Peso:", elemento.peso, "- Valor:", elemento.valor)
