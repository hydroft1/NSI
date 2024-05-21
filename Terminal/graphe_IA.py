# CHAT GPT 4.o
from collections import deque, defaultdict

def contient_cycle(graphe):
    def bfs_cycle_check(start):
        queue = deque([(start, -1)])  # (current_node, parent_node)
        visited[start] = True
        
        while queue:
            current, parent = queue.popleft()
            
            for neighbor in graphe[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current))
                elif neighbor != parent:
                    return True
        return False
    
    visited = defaultdict(bool)
    
    for node in graphe:
        if not visited[node]:
            if bfs_cycle_check(node):
                return True
    return False

# Exemple d'utilisation
graphe = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

print(contient_cycle(graphe))  # Affiche True s'il y a un cycle, False sinon

# Llama 3 70B
from collections import deque

def has_cycle(graph):
    """
    Retourne True si le graphe contient un cycle, False sinon.
    """
    visited = set()
    queue = deque()

    for node in graph:
        if node not in visited:
            queue.append(node)
            visited.add(node)
            while queue:
                current_node = queue.popleft()
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                    else:
                        # Si le voisin a déjà été visité, c'est que nous avons trouvé un cycle
                        return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(has_cycle(graph))  # Retourne True car le graphe contient un cycle
