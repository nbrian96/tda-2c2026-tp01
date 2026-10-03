# TRABAJO PRÁCTICO 1

---

## PROBLEMA 1 – FUERZA BRUTA vs. BACKTRACKING

1. Diseñar e implementar un algoritmo que resuelva el problema de la mochila mediante **fuerza bruta**.
2. Luego, modificarlo para que, mediante **backtracking**, llegue al mismo resultado en menos tiempo.
3. Calcular el orden de complejidad temporal de los algoritmos desarrollados.
4. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real en ambos algoritmos.

### Requisitos
 
- Python 3.6 o superior
- matplotlib (solo para `grafico.py`):
```bash
pip install matplotlib
```
 
### Ejecución
 
Desde la carpeta del proyecto:
 
```bash
# Resolver Mochilas/mochila5.txt con fuerza bruta y backtracking
python codigo.py
 
# Generar un archivo de mochila aleatorio
python crear_mochila.py
 
# Medir tiempos y generar tiempos.csv y grafico.png
python grafico.py
```
 
En Linux/macOS usar `python3` en lugar de `python`.

---

## PROBLEMA 2 – GREEDY

1. Diseñar e implementar un algoritmo **greedy** que resuelva el problema de la mochila. Dicho algoritmo debe tener garantía de calidad \(1/2\).
2. Calcular el orden de complejidad temporal del algoritmo desarrollado.
3. Aplicarlo a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real.
4. Aplicarlo a un set de datos creado manualmente donde actúe la garantía de calidad.

### Requisitos
 
- Python 3.7 o superior
- No necesita instalar bibliotecas externas
- `problema02.py` y `crear_mochila.py` deben estar en la misma carpeta

### Ejecución
 
Desde la carpeta del proyecto:
 
```bash
# Ejemplo manual de 7 elementos (capacidad 100), donde actúa la garantía
python problema02.py
 
# Generar una mochila aleatoria de n elementos y resolverla (ej: 1000)
python problema02.py 1000
 
# Resolver una mochila desde un archivo
python problema02.py mochila1000.txt
```
 
En Linux/macOS usar `python3` en lugar de `python`.

---

## PROBLEMA 3 – PROGRAMACIÓN DINÁMICA

1. Diseñar e implementar dos algoritmos que resuelvan el problema de la mochila mediante **programación dinámica**:
   - Uno de los algoritmos deberá resolverlo con el **planteo tradicional** (maximizar el beneficio para una capacidad fija).
   - El otro deberá resolverlo con el **planteo alternativo** (minimizar el peso para un beneficio fijo).
2. Calcular el orden de complejidad temporal de los algoritmos desarrollados.
3. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real en ambos algoritmos.
4. Aplicar ambos algoritmos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar los tiempos de ejecución de ambos algoritmos. Analizar los resultados obtenidos.

## Requisitos
 
- Python 3.6 o superior
- matplotlib (solo para generar los gráficos):
```bash
pip install matplotlib
```
 
- `crear_mochila.py` debe estar en la **carpeta anterior** a la de este problema (`generar_datos.py` lo importa desde `..`).
- Memoria RAM: el algoritmo alternativo con n = 1000 construye una matriz de ~500 millones de posiciones y necesita varios GB de RAM libres.
Estructura esperada:
 
```
.
├── crear_mochila.py
└── problema03/
    ├── generar_datos.py
    ├── medir_tiempos.py
    ├── mochila_tradicional.py
    ├── mochila_alternativo.py
    └── graficar.py
```
 
## Ejecución
 
Desde la carpeta `problema03/`, en este orden:
 
```bash
# 1. Generar los sets de datos (mochila10.txt ... mochila1000.txt)
python generar_datos.py
 
# 2. Medir tiempos (genera res_tradicional.txt y res_alternativo.txt)
python medir_tiempos.py
 
# 3. Generar los gráficos (tradicional.png, alternativo.png, comparacion.png)
python graficar.py
```


### Resolver una sola mochila
 
```bash
python mochila_tradicional.py mochila10.txt
python mochila_alternativo.py mochila10.txt
```
 
Cada comando imprime el beneficio máximo. Ambos deben dar el mismo valor.
 
En Linux/macOS usar `python3` en lugar de `python`.

---

## PROBLEMA 4 – PROGRAMACIÓN LINEAL

1. Diseñar e implementar un algoritmo que resuelva el problema de la mochila mediante **programación lineal entera** utilizando la biblioteca `PuLP`.
2. Calcular el orden de complejidad temporal del algoritmo desarrollado.
3. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real.

---


## Requisitos
 
- Python 3.9 o superior
- PuLP (incluye el solver CBC) y matplotlib:
```bash
pip install pulp matplotlib
```
 
- `crear_mochila.py` debe estar en la **carpeta anterior** a la de este problema (`generar_datos.py` lo importa desde `..`).
Estructura esperada:
 
```
.
└── problema04/
    ├── generar_datos.py
    ├── graficar_tiempos.py
    └── problema04.py
```
 
## Ejecución
 
Desde la carpeta `problema04/`, en este orden:
 
```bash
# 1. Generar los sets de datos (mochila10.txt, mochila100.txt, ...)
python generar_datos.py
 
# 2. Medir tiempos del solver y generar resultados_PL.txt y tiempos_PL.png
python graficar_tiempos.py
```
 
`problema04.py` contiene las funciones del modelo (`leer_mochila`, `construir_modelo`, `resolver_mochila`) y es importado por `graficar_tiempos.py`; no se ejecuta por separado.
 
Los tamaños a evaluar están en `TAMANIOS` dentro de `generar_datos.py`. Los tamaños grandes pueden tardar mucho, así que para una prueba rápida conviene reducir la lista (por ejemplo, `[10, 100, 1000]`).
 
En Linux/macOS usar `python3` en lugar de `python`.

## CONCLUSIÓN

- Comparar en los rangos en que sea posible los tiempos obtenidos para los mismos problemas por los 6 algoritmos desarrollados.
- Analizar los resultados obtenidos.

---

## CONDICIONES GENERALES DE LOS PROBLEMAS

Para cada algoritmo, se debe incluir:

- **Supuestos:** Identificar supuestos, condiciones, limitaciones y/o premisas bajo los cuales funcionará el algoritmo desarrollado.
- **Diseño:**
  - Incluir un Pseudocódigo.
  - Detallar las estructuras de datos utilizadas.
- **Seguimiento:** Ejemplo de seguimiento con un set de datos reducido.
- **Complejidad:** Análisis de la complejidad temporal a partir del pseudocódigo.
- **Sets de datos:** Adjuntar los sets de datos utilizados. Indicar los criterios con que se tomaron.
- **Tiempos de Ejecución:** Medir los tiempos de ejecución de cada set de datos y presentarlos en un gráfico.
- **Informe de Resultados:** Redactar un informe de resultados comparando los tiempos de ejecución. ¿Se corresponde con la complejidad determinada inicialmente? El gráfico comparativo de tiempos debe incluir tanto la curva con los valores medidos como la curva teórica de ajuste.

---

## CONDICIONES GENERALES DE ENTREGA

El trabajo debe ser entregado en un archivo `.zip` conteniendo:

1. **Documento:**
   - Carátula, índice y numeración de páginas.
   - La carátula debe incluir nombre y padrón de los integrantes del grupo.
   - Debe presentarse en formato **PDF**.
2. **Archivos de código fuente:**
   - Fuentes desarrollados.
   - Indicar en el documento el lenguaje de programación utilizado e incluir instrucciones para compilar (de ser necesario) y ejecutar.
3. **Archivos con los sets de datos utilizados.**
4. **Archivos con resultados obtenidos para cada set de datos.**
5. **Referencias bibliográficas:** Si se incluyeran, utilizar normas **APA 7ma edición**.

## Ramas del repositorio

Este proyecto utiliza un flujo de trabajo basado en ramas para organizar el desarrollo individual y la integración del equipo.

### 🔹 Ramas principales

- **Master**
  - Rama estable del proyecto.
  - Contiene versiones listas para entrega.

- **Entrega**
  - Rama de integración.
  - Aquí se unen los cambios de las ramas de trabajo individuales.
  - Representa la versión más actual del proyecto en desarrollo.

### Ramas de desarrollo (feature branches)

Cada integrante trabaja en su propia rama:

- `Greedy`
- `lineal`
- `Backtracking`
- `Pd`

Cada una contiene el trabajo individual antes de ser integrado a `Entrega`.

---

## Flujo de trabajo

### 1. Actualizar rama develop

Antes de empezar a trabajar:

```bash
git checkout Entrega
git pull origin Entrega
```

### 2. Actualizar tu rama de trabajo

Cambiar a tu rama de desarrollo:
```bash
git checkout rama_problema
```

Traer los últimos cambios de entrega:
```bash
git pull --rebase origin entrega
```

### 3. Trabajar en la feature

Realizar los cambios necesarios en el código.
```bash
git add .
git commit -m "Descripción clara del cambio realizado"
```

### 4. Subir los cambios a tu rama

Una vez quieras guardar tus cambios, los guardas en tu rama:
```bash
git push origin rama_problema
```

### 5. Integrar cambios a la rama entrega

Cuando la funcionalidad esté lista para integrarse:

Cambiar a la rama entrega:
```bash
git checkout Entrega
```

Actualiza la rama entrega:
```bash
git pull origin Entrega
```

Fusionar la rama de trabajo feature con la rama entrega:
```bash
git merge rama_problema
```

Subir la versión integrada:
```bash
git push origin Entrega
```
