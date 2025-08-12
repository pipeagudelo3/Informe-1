#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from collections import defaultdict

# Definición de trabajos y sus operaciones: (máquina, duración)
jobs = {
    'J1': [('M1', 3), ('M2', 2), ('M3', 2)],
    'J2': [('M2', 2), ('M1', 4), ('M3', 3)],
    'J3': [('M3', 3), ('M2', 3), ('M1', 2)],
    'J4': [('M1', 2), ('M3', 1), ('M2', 4)],
    'J5': [('M2', 4), ('M3', 3), ('M1', 3)]
}

machines = ['M1', 'M2', 'M3']

# Lista total de operaciones codificadas como (job_id, operation_index)
all_operations = []
for job, ops in jobs.items():
    for idx in range(len(ops)):
        all_operations.append((job, idx))


# ## Construir cronograma y calcular tiempo de ejecución (makespan)

# In[2]:


def build_schedule(individual):
    job_ready_time = defaultdict(int)
    machine_ready_time = defaultdict(int)
    schedule = {}

    for (job, op_idx) in individual:
        machine, duration = jobs[job][op_idx]
        start_time = max(job_ready_time[job], machine_ready_time[machine])
        end_time = start_time + duration

        schedule[(job, op_idx)] = (start_time, end_time)
        job_ready_time[job] = end_time
        machine_ready_time[machine] = end_time

    return schedule

def makespan(schedule):
    return max(end for (_, end) in schedule.values())


# ## Generar individuos válidos

# In[3]:


def generate_individual():
    job_counters = {job: 0 for job in jobs}
    ops = []
    pending = []

    # Añadir una operación inicial de cada trabajo
    for job in jobs:
        pending.append((job, 0))

    while pending:
        op = random.choice(pending)
        ops.append(op)
        job, idx = op
        pending.remove(op)
        if idx + 1 < len(jobs[job]):
            pending.append((job, idx + 1))
    return ops

def create_population(size=10):
    return [generate_individual() for _ in range(size)]


# ## Fitness y operadores genéticos

# In[4]:


def fitness(individual):
    schedule = build_schedule(individual)
    return -makespan(schedule)  # Negativo porque el GA maximiza

def selection(population):
    a, b = random.sample(population, 2)
    return a if fitness(a) > fitness(b) else b

def crossover(p1, p2):
    size = len(p1)
    cut1, cut2 = sorted(random.sample(range(size), 2))
    middle = p1[cut1:cut2]
    remaining = [op for op in p2 if op not in middle]
    child = remaining[:cut1] + middle + remaining[cut1:]
    return child

def mutate(ind, prob=0.2):
    if random.random() < prob:
        i, j = random.sample(range(len(ind)), 2)
        ind[i], ind[j] = ind[j], ind[i]
    return ind


# ## Ciclo evolutivo

# In[5]:


def evolve(population, generations=30):
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
        print(f"Gen {gen+1:2d} | Makespan: {-fitness(best)}")
    return best

# Ejecutar
population = create_population(10)
best_solution = evolve(population)


# ## Visualización de la mejor solución

# In[6]:


print("\n Mejor programación encontrada:")
schedule = build_schedule(best_solution)
for op, (start, end) in sorted(schedule.items(), key=lambda x: x[1][0]):
    job, idx = op
    machine = jobs[job][idx][0]
    print(f"{job} Op{idx+1} en {machine}: {start} → {end}")

print(f"\n🕒 Makespan total: {makespan(schedule)}")


# In[7]:


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_gantt(schedule):
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = plt.cm.tab20.colors
    machine_y = {'M1': 3, 'M2': 2, 'M3': 1}

    for i, ((job, op_idx), (start, end)) in enumerate(schedule.items()):
        machine, duration = jobs[job][op_idx]
        y = machine_y[machine]
        color = colors[hash(job) % len(colors)]

        ax.barh(y, end - start, left=start, height=0.5, color=color, edgecolor='black')
        ax.text(start + 0.2, y, f'{job}-Op{op_idx+1}', va='center', ha='left', color='black', fontsize=8)

    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['M3', 'M2', 'M1'])
    ax.set_xlabel('Tiempo')
    ax.set_title('Diagrama de Gantt de la programación')
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Mostrar Gantt
plot_gantt(schedule)

