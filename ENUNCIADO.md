# TRABAJO PRÁCTICO 1

---

## PROBLEMA 1 – FUERZA BRUTA vs. BACKTRACKING

1. Diseñar e implementar un algoritmo que resuelva el problema de la mochila mediante **fuerza bruta**.
2. Luego, modificarlo para que, mediante **backtracking**, llegue al mismo resultado en menos tiempo.
3. Calcular el orden de complejidad temporal de los algoritmos desarrollados.
4. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real en ambos algoritmos.

---

## PROBLEMA 2 – GREEDY

1. Diseñar e implementar un algoritmo **greedy** que resuelva el problema de la mochila. Dicho algoritmo debe tener garantía de calidad \(1/2\).
2. Calcular el orden de complejidad temporal del algoritmo desarrollado.
3. Aplicarlo a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real.
4. Aplicarlo a un set de datos creado manualmente donde actúe la garantía de calidad.

---

## PROBLEMA 3 – PROGRAMACIÓN DINÁMICA

1. Diseñar e implementar dos algoritmos que resuelvan el problema de la mochila mediante **programación dinámica**:
   - Uno de los algoritmos deberá resolverlo con el **planteo tradicional** (maximizar el beneficio para una capacidad fija).
   - El otro deberá resolverlo con el **planteo alternativo** (minimizar el peso para un beneficio fijo).
2. Calcular el orden de complejidad temporal de los algoritmos desarrollados.
3. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real en ambos algoritmos.
4. Aplicar ambos algoritmos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar los tiempos de ejecución de ambos algoritmos. Analizar los resultados obtenidos.

---

## PROBLEMA 4 – PROGRAMACIÓN LINEAL

1. Diseñar e implementar un algoritmo que resuelva el problema de la mochila mediante **programación lineal entera** utilizando la biblioteca `PuLP`.
2. Calcular el orden de complejidad temporal del algoritmo desarrollado.
3. Aplicarlos a diferentes sets de datos obtenidos con el código adjunto `crear_mochila.py`, de tamaños adecuados para poder comparar la curva de tiempos de ejecución teórica y real.

---

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
