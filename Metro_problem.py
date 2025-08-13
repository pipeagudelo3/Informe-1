from collections import deque
import time
import tracemalloc

metro = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "H", "I"],
    "F": ["C", "J"],
    "G": ["D"],
    "H": ["E"],
    "I": ["E", "J"],
    "J": ["F", "I"]
}

class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
    
    def path(self):
        node, p = self, []
        while node:
            p.append(node.state)
            node = node.parent
        return list(reversed(p))


class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return self.graph[state]

    def goal_test(self, state):
        return state == self.goal


def bfs(problem):
    start_time = time.time()
    tracemalloc.start()
    
    frontier = deque([Node(problem.initial)])
    explored = set()
    
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return node.path(), time.time() - start_time, mem
        
        explored.add(node.state)
        for action in problem.actions(node.state):
            if action not in explored and all(n.state != action for n in frontier):
                frontier.append(Node(action, node))

def dls(node, problem, limit, explored):
    if problem.goal_test(node.state):
        return node
    elif limit == 0:
        return None
    else:
        explored.add(node.state)
        for action in problem.actions(node.state):
            if action not in explored:
                result = dls(Node(action, node, node.depth+1), problem, limit-1, explored)
                if result:
                    return result
        return None

def ids(problem):
    start_time = time.time()
    tracemalloc.start()
    
    depth = 0
    while True:
        explored = set()
        result = dls(Node(problem.initial), problem, depth, explored)
        if result:
            mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return result.path(), time.time() - start_time, mem
        depth += 1

problem = Problem("F", "G", metro)

ruta_bfs, tiempo_bfs, mem_bfs = bfs(problem)
ruta_ids, tiempo_ids, mem_ids = ids(problem)

print("BFS → Ruta:", ruta_bfs, "Tiempo:", tiempo_bfs, "Memoria:", mem_bfs)
print("IDS → Ruta:", ruta_ids, "Tiempo:", tiempo_ids, "Memoria:", mem_ids)
