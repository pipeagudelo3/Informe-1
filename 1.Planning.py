#!/usr/bin/env python
# coding: utf-8

# In[66]:


import random

# --- Datos del problema ---
tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
precedence = {
    'C': ['A'],
    'D': ['A'],
    'E': ['B'],
    'F': ['C', 'D'],
    'G': ['E', 'F'],
    'H': ['G'],
    'I': ['F'],
    'J': ['H', 'I']
}

def is_valid(order):
    position = {task: i for i, task in enumerate(order)}
    for task, preds in precedence.items():
        for pred in preds:
            if position[pred] > position[task]:
                return False
    return True

def fitness(order):
    position = {task: i for i, task in enumerate(order)}
    score = 100
    for task, preds in precedence.items():
        for pred in preds:
            if position[pred] > position[task]:
                score -= 30
            else:
                # Penalizar distancia grande entre pred y task
                score -= (position[task] - position[pred] - 1) * 2
    return score


# ## Generar población

# In[67]:


def create_individual():
    return random.sample(tasks, len(tasks))

def create_population(size=20):
    return [create_individual() for _ in range(size)]

population = create_population()
for ind in population:
    print(ind, "-> Fitness:", fitness(ind))


# ## Operadores GA: selección, cruce, mutación

# In[68]:


def selection(pop):
    a, b = random.sample(pop, 2)
    return a if fitness(a) > fitness(b) else b

def crossover(p1, p2):
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = p1[start:end]
    fill = [x for x in p2 if x not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child

def mutate(ind, prob=0.2):
    if random.random() < prob:
        i, j = random.sample(range(len(ind)), 2)
        ind[i], ind[j] = ind[j], ind[i]
    return ind


# ## Evolución

# In[69]:


def evolve(population, generations=50):
    for gen in range(generations):
        new_pop = []
        for _ in range(len(population)):
            p1 = selection(population)
            p2 = selection(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop
        best = max(population, key=fitness)
        print(f"Gen {gen+1:2d}: {best} | Fitness: {fitness(best)} | Válido: {is_valid(best)}")
    return best

best = evolve(population)
print("\nMejor solución encontrada:", best)

