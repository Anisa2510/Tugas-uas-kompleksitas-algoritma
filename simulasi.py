import heapq
from collections import deque

# ==============================
# GRAF: Representasi Peta Kota
# ==============================
graph = {
    'A': {'B': 7, 'C': 9},
    'B': {'A': 7, 'D': 10, 'E': 15},
    'C': {'A': 9, 'F': 11},
    'D': {'B': 10, 'E': 6},
    'E': {'B': 15, 'D': 6, 'H': 9},
    'F': {'C': 11, 'G': 2},
    'G': {'F': 2, 'H': 1},
    'H': {'G': 1, 'E': 9}
}

# ==============================
# BFS TRAVERSAL
# ==============================
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

# ==============================
# DFS TRAVERSAL
# ==============================
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# ==============================
# DIJKSTRA (Shortest Path)
# ==============================
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)
        if dist > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# ==============================
# BELLMAN-FORD (Shortest Path)
# ==============================
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]

    # Cek siklus negatif
    for u in graph:
        for v in graph[u]:
            if distances[u] + graph[u][v] < distances[v]:
                print("Terdapat siklus berbobot negatif.")
                return None
    return distances

# ==============================
# SIMULASI DARI SIMPUL TERPILIH
# ==============================
start_node = 'A'

# Traversal
print("=== Simulasi Traversal dari simpul A ===")
bfs(graph, start_node)

print("DFS:", end=" ")
dfs(graph, start_node)
print("\n")

# Pencarian rute terpendek
print("=== Dijkstra dari A ===")
dijkstra_result = dijkstra(graph, start_node)
for node, dist in dijkstra_result.items():
    print(f"Jarak dari A ke {node}: {dist} km")

print("\n=== Bellman-Ford dari A ===")
bellman_result = bellman_ford(graph, start_node)
if bellman_result:
    for node, dist in bellman_result.items():
        print(f"Jarak dari A ke {node}: {dist} km")
