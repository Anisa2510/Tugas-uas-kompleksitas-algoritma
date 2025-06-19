import heapq

# Representasi graf berbobot menggunakan adjacency list
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'F': 11},
    'E': {'D': 4},
    'F': {}
}

# ===============================
# ALGORITMA DIJKSTRA
# ===============================
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# ===============================
# ALGORITMA BELLMAN-FORD
# ===============================
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
                print("Graph mengandung siklus berbobot negatif.")
                return None

    return distances

# ===============================
# PEMANGGILAN FUNGSI
# ===============================
start_node = 'A'

print("=== Dijkstra ===")
dijkstra_result = dijkstra(graph, start_node)
for node in dijkstra_result:
    print(f"Jarak dari {start_node} ke {node}: {dijkstra_result[node]}")

print("\n=== Bellman-Ford ===")
bellman_result = bellman_ford(graph, start_node)
if bellman_result:
    for node in bellman_result:
        print(f"Jarak dari {start_node} ke {node}: {bellman_result[node]}")
