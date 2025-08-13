
# Ejercicio 2
# Ruta óptima a Bucharest usando A* Search

## Autor
Felipe Agudelo y Juan Manuel  
Universidad EAFIT  
Curso: Inteligencia Artificial  
Semana 2 - Informe 1

---

## Análisis del problema

Este proyecto resuelve el problema de encontrar la ruta más corta desde una ciudad inicial (Arad) hasta Bucharest en el mapa de Rumania. Cada ciudad está conectada por carreteras con un costo asociado (distancia en kilómetros). El objetivo es minimizar el costo total del viaje.

El problema se modela como un grafo, donde:

- Los **nodos** son ciudades.
- Las **acciones** son movimientos entre ciudades conectadas.
- El **costo** es la distancia entre ciudades.
- El **estado inicial** es `'Arad'`.
- El **estado objetivo** es `'Bucharest'`.

---

## Aplicación del algoritmo A* Search

Se implementó el algoritmo A* Search, que combina:

- `g(n)`: el costo acumulado desde el inicio hasta el nodo actual.
- `h(n)`: una heurística que estima la distancia restante hasta Bucharest.

La función de evaluación utilizada es:

f(n) = g(n) + h(n)


La heurística empleada es la distancia en línea recta desde cada ciudad hasta Bucharest, lo que garantiza que sea admisible (nunca sobreestima el costo real) y consistente.

---

## Justificación de la eleccion de la ruta optima

La heurística utilizada cumple con las condiciones necesarias para que A* encuentre la ruta óptima:

- Admisibilidad: nunca sobreestima el costo real.
- Consistencia: la estimación entre nodos es coherente con los costos reales.

Por lo tanto, la ruta encontrada por A* es la más corta posible en términos de distancia total.

---


=======
# Ruta óptima a Bucharest usando A* Search

## Autor
Felipe Agudelo y Juan Manuel Lopez
Universidad EAFIT  
Curso: Inteligencia Artificial  
Semana 2 - Informe 1

---

## Análisis del problema

Este proyecto resuelve el problema de encontrar la ruta más corta desde una ciudad inicial (Arad) hasta Bucharest en el mapa de Rumania. Cada ciudad está conectada por carreteras con un costo asociado (distancia en kilómetros). El objetivo es minimizar el costo total del viaje.

El problema se modela como un grafo, donde:

- Los **nodos** son ciudades.
- Las **acciones** son movimientos entre ciudades conectadas.
- El **costo** es la distancia entre ciudades.
- El **estado inicial** es `'Arad'`.
- El **estado objetivo** es `'Bucharest'`.

---

## Aplicación del algoritmo A* Search

Se implementó el algoritmo A* Search, que combina:

- `g(n)`: el costo acumulado desde el inicio hasta el nodo actual.
- `h(n)`: una heurística que estima la distancia restante hasta Bucharest.

La función de evaluación utilizada es:

f(n) = g(n) + h(n)


La heurística empleada es la distancia en línea recta desde cada ciudad hasta Bucharest, lo que garantiza que sea admisible (nunca sobreestima el costo real) y consistente.

---

## Justificación de la eleccion de la ruta optima

La heurística utilizada cumple con las condiciones necesarias para que A* encuentre la ruta óptima:

- Admisibilidad: nunca sobreestima el costo real.
- Consistencia: la estimación entre nodos es coherente con los costos reales.

Por lo tanto, la ruta encontrada por A* es la más corta posible en términos de distancia total.

------------------------------------------------------------------------------------------------

# Ejercicio 3

Cuando un laberinto presenta múltiples salidas posibles, el algoritmo de búsqueda debe adaptarse para:

- Identificación de salidas
Las salidas se definen como celdas accesibles ubicadas en los bordes del laberinto. Antes de iniciar la búsqueda, se recorre el perímetro del laberinto para detectar todas las posiciones que cumplen con esta condición.

- Modificación del algoritmo de búsqueda
El algoritmo debe ser modificado para continuar la exploración hasta encontrar todas las salidas alcanzables desde el punto de inicio. En lugar de detenerse en la primera salida encontrada, se almacenan todos los caminos posibles hacia cada salida.

- Selección del camino óptimo
Una vez identificados los caminos hacia las distintas salidas, se aplica un criterio de selección según el objetivo deseado:

Camino más corto: minimiza el número de pasos.

Camino más seguro: evita zonas peligrosas o bloqueadas.

Camino más eficiente: optimiza recursos como tiempo o energía.


## 4

Al modificar el laberinto por uno más grande, se incrementa significativamente la complejidad del problema de búsqueda. El algoritmo actual está diseñado para encontrar el camino con el menor costo total, lo que lo lleva a evitar sistemáticamente cualquier tipo de terreno que implique penalización, como barro (~) o fuego (^). Esta estrategia es eficiente si el objetivo es minimizar recursos, pero puede no ser adecuada en todos los contextos. Por ejemplo, si el objetivo fuera encontrar el camino más corto en número de pasos, o incluso el más costoso (por razones estratégicas o de simulación), la función de costo debería adaptarse para reflejar ese nuevo criterio. Esto implica modificar tanto la función action_cost como el enfoque del algoritmo: en lugar de priorizar el menor costo acumulado, se podría priorizar la menor cantidad de movimientos, o incluso maximizar el costo total si se desea simular un recorrido por zonas de alto riesgo. Esta flexibilidad es clave para adaptar el algoritmo a distintos tipos de laberintos y objetivos, pero también revela una limitación: el algoritmo actual está acoplado a una única estrategia de optimización, y requiere ajustes explícitos para cambiar su comportamiento.

