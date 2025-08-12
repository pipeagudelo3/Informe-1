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


