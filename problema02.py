from __future__ import annotations

import os
import sys
from dataclasses import dataclass

import crear_mochila


@dataclass
class Elemento:
    id: int
    peso: int
    valor: int

    @property
    def ratio(self) -> float:
        return self.valor / self.peso if self.peso > 0 else 0.0


@dataclass
class ResultadoMochila:
    valor_total: int
    peso_total: int
    elementos_seleccionados: list[Elemento]
    actuo_garantia: bool


def obtener_mochila_manual_garantia() -> tuple[int, list[Elemento]]:
    capacidad = 100
    elementos = [
        Elemento(1, 5, 10),
        Elemento(2, 5, 10),
        Elemento(3, 10, 18),
        Elemento(4, 10, 16),
        Elemento(5, 75, 110),
        Elemento(6, 40, 40),
        Elemento(7, 40, 36),
    ]
    return capacidad, elementos


def cargar_mochila_desde_archivo(ruta_archivo: str) -> tuple[int, list[Elemento]]:
    elementos = []
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        primera_linea = f.readline().strip()
        if not primera_linea:
            return 0, []
        capacidad = int(primera_linea)

        for i, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            peso, valor = linea.split(",")
            elementos.append(Elemento(i, int(peso.strip()), int(valor.strip())))
    return capacidad, elementos


def generar_mochila(n: int) -> tuple[int, list[Elemento]]:
    crear_mochila.crear_mochila(n)
    return cargar_mochila_desde_archivo(f"mochila{n}.txt")


def resolver_mochila_greedy(capacidad: int, elementos: list[Elemento]) -> ResultadoMochila:
    candidatos = [elem for elem in elementos if elem.peso <= capacidad]
    if not candidatos:
        return ResultadoMochila(0, 0, [], False)

    candidatos.sort(key=lambda e: (e.ratio, e.valor), reverse=True)

    solucion_voraz: list[Elemento] = []
    peso_voraz = 0
    valor_voraz = 0
    elemento_critico: Elemento | None = None

    for elem in candidatos:
        if peso_voraz + elem.peso <= capacidad:
            solucion_voraz.append(elem)
            peso_voraz += elem.peso
            valor_voraz += elem.valor
        elif elemento_critico is None:
            elemento_critico = elem

    if elemento_critico is not None and elemento_critico.valor > valor_voraz:
        return ResultadoMochila(
            valor_total=elemento_critico.valor,
            peso_total=elemento_critico.peso,
            elementos_seleccionados=[elemento_critico],
            actuo_garantia=True,
        )

    return ResultadoMochila(
        valor_total=valor_voraz,
        peso_total=peso_voraz,
        elementos_seleccionados=solucion_voraz,
        actuo_garantia=False,
    )


def main():
    if len(sys.argv) == 1:
        capacidad, elementos = obtener_mochila_manual_garantia()
    elif sys.argv[1].isdigit():
        capacidad, elementos = generar_mochila(int(sys.argv[1]))
    elif os.path.isfile(sys.argv[1]):
        capacidad, elementos = cargar_mochila_desde_archivo(sys.argv[1])
    else:
        print("Uso: python3 problema02.py [n | archivo.txt]")
        sys.exit(1)

    resultado = resolver_mochila_greedy(capacidad, elementos)

    print(f"Capacidad: {capacidad}")
    print(f"Elementos: {len(resultado.elementos_seleccionados)} / {len(elementos)}")
    print(f"Peso:      {resultado.peso_total}")
    print(f"Valor:     {resultado.valor_total}")
    print(f"Garantía:  {'SÍ' if resultado.actuo_garantia else 'NO'}")


if __name__ == "__main__":
    main()
