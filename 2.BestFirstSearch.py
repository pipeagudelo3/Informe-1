
#!/usr/bin/env python
# coding: utf-8

# **ALGORITMOS DE BUSQUEDA-Best-First Search**

# In[ ]:


import heapq #El módulo heapq para implementar colas de prioridad (heaps)


# In[ ]:


class Node: #definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state #El estado que define el nodo (ciudad actual)
        self.parent = parent #El nodo padre de donde se origina el nodo actual (estado-ciudad anterior)
        self.action = action #Action tomada desde el padre para llegar al nodo (accion que realiza el nodo)
        self.path_cost = path_cost #costo desde el nodo raiz (estado inicial), hasta el nodo actual (costo acumulado de las acciones realizadas)

    def __lt__(self, other): #comparar dos objetos de clase node basado en el costo
        return self.path_cost < other.path_cost


# In[ ]:


def expand(problem, node):
    children = []
    for action in problem.actions(node.state):
        result_state = problem.result(node.state, action)
        cost = node.path_cost + problem.action_cost(node.state, action, result_state)
        child = Node(result_state, node, action, cost)
        children.append(child)
    return children 


# In[ ]:


class Problem: #DEFINICION DEL PROBLEMA
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.actions = actions #acciones disponibles desde un estado.
        self.result = result  #estado resultante de aplicar una acción
        self.action_cost = action_cost #costo de una acción
        self.is_goal = is_goal #verificación de si el estado es el estado objetivo


# In[ ]:


def best_first_search(problem, f):
    node = Node(state=problem.initial) #Crea el nodo raíz con el estado inicial del problema.
    frontier = [(f(node), node)]  # frontera como una cola de prioridad (f(n)) con el nodo inicial.
    heapq.heapify(frontier) # Convierte la lista frontier en una cola de prioridad (heap)
    reached = {problem.initial: node} #registrar los estados alcanzados y su nodo correspondiente.

    while frontier:
        _, node = heapq.heappop(frontier) #Extrae el nodo con el valor mínimo de f de la frontera.
        if problem.is_goal(node.state):   #Si el estado del nodo es el estado objetivo, devuelve el nodo.
            return node

        for child in expand(problem, node): #Expande el nodo generando sus nodos hijos.
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost: #Si el estado del nodo hijo no ha sido alcanzado antes o si se alcanza con un costo de camino menor, actualiza el dict y añade el nodo hijo a la frontera.
                reached[s] = child
            heapq.heappush(frontier, (f(child), child)) # Añade el nodo hijo a la frontera

    return None  #Se exploran todos los nodos posibles, y no se encuentra una solución solución


# In[ ]:


def result(state, action):
    return action

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))#En el caso de que no se encuentre un costo, el valor sera infinito

def is_goal(state):
    return state == goal

def f(node):
    return node.path_cost + heuristic.get(node.state, float('inf'))
 

initial = 'Arad'
goal = 'Bucharest'

actions = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Zerind': ['Arad', 'Oradea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Pitesti': ['Rimnicu Vilcea', 'Bucharest'],
        'Craiova': ['Rimnicu Vilcea', 'Drobeta', 'Pitesti'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Urziceni', 'Giurgiu'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']


}


action_costs = {
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Arad', 'Zerind'): 75,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Timisoara', 'Lugoj'): 111,
    ('Zerind', 'Oradea'): 71,
    ('Fagaras', 'Bucharest'): 211,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Lugoj', 'Mehadia'): 70,
    ('Oradea', 'Sibiu'): 151,
    ('Pitesti', 'Bucharest'): 101,
    ('Craiova', 'Drobeta'): 120,
    ('Craiova', 'Pitesti'): 138,
    ('Mehadia', 'Drobeta'): 75,
    ('Bucharest', 'Urziceni'): 85,
    ('Bucharest', 'Giurgiu'): 90,
    ('Urziceni', 'Hirsova'): 98,
    ('Urziceni', 'Vaslui'): 142,
    ('Hirsova', 'Eforie'): 86,
    ('Vaslui', 'Iasi'): 92,
    ('Iasi', 'Neamt'): 87
}

heuristic = {
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
    'Oradea': 380,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 178,
    'Pitesti': 98,
    'Bucharest': 0
}


problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal)
solution = best_first_search(problem, f)#Resultado del algoritmo best_first_search aplicado al problema definido.

if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")

#!/usr/bin/env python
# coding: utf-8

# **ALGORITMOS DE BUSQUEDA-Best-First Search**

# In[ ]:


import heapq #El módulo heapq para implementar colas de prioridad (heaps)


# In[ ]:


class Node: #definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state #El estado que define el nodo (ciudad actual)
        self.parent = parent #El nodo padre de donde se origina el nodo actual (estado-ciudad anterior)
        self.action = action #Action tomada desde el padre para llegar al nodo (accion que realiza el nodo)
        self.path_cost = path_cost #costo desde el nodo raiz (estado inicial), hasta el nodo actual (costo acumulado de las acciones realizadas)

    def __lt__(self, other): #comparar dos objetos de clase node basado en el costo
        return self.path_cost < other.path_cost


# In[ ]:


def expand(problem, node):
    children = []
    for action in problem.actions(node.state):
        result_state = problem.result(node.state, action)
        cost = node.path_cost + problem.action_cost(node.state, action, result_state)
        child = Node(result_state, node, action, cost)
        children.append(child)
    return children 


# In[ ]:


class Problem: #DEFINICION DEL PROBLEMA
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.actions = actions #acciones disponibles desde un estado.
        self.result = result  #estado resultante de aplicar una acción
        self.action_cost = action_cost #costo de una acción
        self.is_goal = is_goal #verificación de si el estado es el estado objetivo


# In[ ]:


def best_first_search(problem, f):
    node = Node(state=problem.initial) #Crea el nodo raíz con el estado inicial del problema.
    frontier = [(f(node), node)]  # frontera como una cola de prioridad (f(n)) con el nodo inicial.
    heapq.heapify(frontier) # Convierte la lista frontier en una cola de prioridad (heap)
    reached = {problem.initial: node} #registrar los estados alcanzados y su nodo correspondiente.

    while frontier:
        _, node = heapq.heappop(frontier) #Extrae el nodo con el valor mínimo de f de la frontera.
        if problem.is_goal(node.state):   #Si el estado del nodo es el estado objetivo, devuelve el nodo.
            return node

        for child in expand(problem, node): #Expande el nodo generando sus nodos hijos.
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost: #Si el estado del nodo hijo no ha sido alcanzado antes o si se alcanza con un costo de camino menor, actualiza el dict y añade el nodo hijo a la frontera.
                reached[s] = child
            heapq.heappush(frontier, (f(child), child)) # Añade el nodo hijo a la frontera

    return None  #Se exploran todos los nodos posibles, y no se encuentra una solución solución


# In[ ]:


def result(state, action):
    return action

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))#En el caso de que no se encuentre un costo, el valor sera infinito

def is_goal(state):
    return state == goal

def f(node):
    return node.path_cost + heuristic.get(node.state, float('inf'))
 

initial = 'Arad'
goal = 'Bucharest'

actions = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Zerind': ['Arad', 'Oradea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Pitesti': ['Rimnicu Vilcea', 'Bucharest'],
        'Craiova': ['Rimnicu Vilcea', 'Drobeta', 'Pitesti'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Urziceni', 'Giurgiu'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']


}


action_costs = {
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Arad', 'Zerind'): 75,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Timisoara', 'Lugoj'): 111,
    ('Zerind', 'Oradea'): 71,
    ('Fagaras', 'Bucharest'): 211,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Lugoj', 'Mehadia'): 70,
    ('Oradea', 'Sibiu'): 151,
    ('Pitesti', 'Bucharest'): 101,
    ('Craiova', 'Drobeta'): 120,
    ('Craiova', 'Pitesti'): 138,
    ('Mehadia', 'Drobeta'): 75,
    ('Bucharest', 'Urziceni'): 85,
    ('Bucharest', 'Giurgiu'): 90,
    ('Urziceni', 'Hirsova'): 98,
    ('Urziceni', 'Vaslui'): 142,
    ('Hirsova', 'Eforie'): 86,
    ('Vaslui', 'Iasi'): 92,
    ('Iasi', 'Neamt'): 87
}

heuristic = {
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
    'Oradea': 380,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 178,
    'Pitesti': 98,
    'Bucharest': 0
}


problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal)
solution = best_first_search(problem, f)#Resultado del algoritmo best_first_search aplicado al problema definido.

if solution:
    path = []
    while solution:
        path.append(solution.state)
        solution = solution.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")



