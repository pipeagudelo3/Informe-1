## Autor
Felipe Agudelo y Juan Manuel Lopera
Universidad EAFIT  
Curso: Inteligencia Artificial  
Semana 2 - Informe 1

# Ejercicio 1
# Ruta óptima a Bucharest usando A* Search
---

## Análisis del problema

Este proyecto resuelve el problema de encontrar la ruta más corta desde una ciudad inicial (Arad) hasta Bucharest en el mapa de Rumania. Cada ciudad está conectada por carreteras con un costo asociado (distancia en kilómetros). El objetivo es minimizar el costo total del viaje.

El problema se modela como un grafo, donde:

- Los **nodos** son ciudades.
- Las **acciones** son movimientos entre ciudades conectadas.
- El **costo** es la distancia entre ciudades.
- El **estado inicial** es `'Arad'`.
- El **estado objetivo** es `'Bucharest'`.

## Aplicación del algoritmo A* Search

Se implementó el algoritmo A* Search, que combina:

- `g(n)`: el costo acumulado desde el inicio hasta el nodo actual.
- `h(n)`: una heurística que estima la distancia restante hasta Bucharest.

La función de evaluación utilizada es:

f(n) = g(n) + h(n)

La heurística empleada es la distancia en línea recta desde cada ciudad hasta Bucharest, lo que garantiza que sea admisible (nunca sobreestima el costo real) y consistente.


## Justificación de la eleccion de la ruta optima

La heurística utilizada cumple con las condiciones necesarias para que A* encuentre la ruta óptima:

- Admisibilidad: nunca sobreestima el costo real.
- Consistencia: la estimación entre nodos es coherente con los costos reales.

Por lo tanto, la ruta encontrada por A* es la más corta posible en términos de distancia total.

---


=======


# Ejercicio 2
# Salida optima del laberinto usando A*

---

## Análisis del problema

Este problema busca crear un buscador de laberintos, el cual se enfoca en llegar desde un inicio "S" hasta una salida "E", mientras que evita los obstaculos marcados por "#" e intenta reducir el costo total de las casillas recorridas, para asi poder encontrar el camino mas corto

El problema se resuelve usando el algoritmo A*, para asi poder encontrar la ruta mas barata desde el punto de inicio hasta el final, se le da una prioridad a las posiciones segun su costo real recorrido mas una estimacion de lo que falta para llegar a la meta, estos valores se guardan mientras se recorren, para asi poder reconstruir el camino mas optimo al final por medio de los parent que se tengan almacenados.

## Comportamiento del algoritmo con cambios en funcion de costo

Dependiendo de los valores que usemos en la funcion de costo, esto podria cambiar totalmente los caminos mas optimos, ya que incluso aunque en terminos de distancia algun camino en especifico sea objetivamente mas corto, si hay variaciones en los costos que podemos encontrar en este camino (Como el barro ~ o el fuego ^) entonces el programa podria determinar que otro camino diferente donde el costo sea menor pero la distancia mayor como el mas optimo.

## Que pasa si hay multiples salidas?

La opcion mas simple podria ser determinar cualquier salida como valida, en ese caso, el programa reconstruiria el camino hacia la primera salida que encuentre, no necesariamente la mas optima pero siempre llegaria a una solucion. La solucion mas optima se basaria en realizar un algoritmo que encuentre todas las salidas y almacene sus costos, para asi poder compararlas entre si, y solo reconstruir el camino hacia la salida con el menor costo, ya que incluso aunque una salida sea mejor en terminos de distancia, tambien debemos considerar los costos debido a los obstaculos que podrian haber como el fuego o el barro, por lo que una salida con mayor distancia podria llegar a ser mas optima siempre y cuando su costo total sea menor.

## Que pasa si el laberinto es mas grande y hay mas obstaculos?

Al modificar el laberinto por uno más grande, se incrementa significativamente la complejidad del problema de búsqueda. El algoritmo actual está diseñado para encontrar el camino con el menor costo total, lo que lo lleva a evitar sistemáticamente cualquier tipo de terreno que implique penalización, como barro (~) o fuego (^). Esta estrategia es eficiente si el objetivo es minimizar recursos, pero puede no ser adecuada en todos los contextos. Por ejemplo, si el objetivo fuera encontrar el camino más corto en número de pasos, o incluso el más costoso (por razones estratégicas o de simulación), la función de costo debería adaptarse para reflejar ese nuevo criterio. Esto implica modificar tanto la función action_cost como el enfoque del algoritmo: en lugar de priorizar el menor costo acumulado, se podría priorizar la menor cantidad de movimientos, o incluso maximizar el costo total si se desea simular un recorrido por zonas de alto riesgo. Esta flexibilidad es clave para adaptar el algoritmo a distintos tipos de laberintos y objetivos, pero también revela una limitación: el algoritmo actual está acoplado a una única estrategia de optimización, y requiere ajustes explícitos para cambiar su comportamiento.

---


=======


# Ejercicio 3
# Navegacion en una red de metro

---

## Análisis del problema

El problema se basa en encontrar la ruta mas corta entre 2 estaciones de metro, pero usando dos enfoques distintos: BFS y IDS

La red de metro esta diseñada como un grafo no dirigido donde todos los pesos entre estaciones son iguales, en donde cada estacion esta representada como un nodo el cual contiene el camino que se ha tomado para llegar hasta ahi, al igual que una clase de problema donde guardamos las acciones que se pueden realizar y la meta a la que debemos llegar.

Usamos BFS para recorrer el grafo por niveles hasta llegar a la meta, y IDS para realizar una busqueda en profundidad mientras que vamos aumentando el limite progresivamente. Teniendo estos 2 algoritmos, comparamos sus resultados en terminos de tiempo y consumo de memoria. (Resultados presentados en el siguiente punto)

## Comparacion de algoritmos

Realizamos 3 pruebas diferentes usando ambos algoritmos, en los 3 casos ambos algoritmos lograron encontrar la ruta mas optima pero tuvieron variaciones en terminos de tiempo y uso de memoria, aqui los datos:

# Primer Prueba, A -> J
BFS → Ruta: ['A', 'C', 'F', 'J'] Tiempo: 0.0005743503570556641 Memoria: (2664, 4616)
IDS → Ruta: ['A', 'C', 'F', 'J'] Tiempo: 3.4809112548828125e-05 Memoria: (1168, 1312)

# Segunda Prueba, A -> H
BFS → Ruta: ['A', 'B', 'E', 'H'] Tiempo: 8.273124694824219e-05 Memoria: (3800, 4616)
IDS → Ruta: ['A', 'B', 'E', 'H'] Tiempo: 2.9325485229492188e-05 Memoria: (728, 904)

# Tercera Prueba, F -> G
BFS → Ruta: ['F', 'C', 'A', 'B', 'D', 'G'] Tiempo: 8.082389831542969e-05 Memoria: (3240, 4616)
IDS → Ruta: ['F', 'C', 'A', 'B', 'D', 'G'] Tiempo: 4.839897155761719e-05 Memoria: (1304, 1544)

Podemos observar que el algoritmo IDS siempre tuvo un menor consumo de memoria en todos los casos. En terminos de tiempo, IDS tambien fue mas rapido en la mayoria de los casos, aunque esto solo se debe al tamaño del grafo que estamos usando, ya que en un sistema mucho mas extenso, BFS terminaria siendo mas efectivo en terminos de tiempo pero aun menos optimo en terminos de memoria, mientras que para IDS seria el caso contrario, el tiempo requerido creceria bastante, pero mantendria su consumo de memoria relativamente bajo cuando lo comparamos con BFS.

---
