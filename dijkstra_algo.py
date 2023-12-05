# Program to understand Dijkstra's algorithm
import heapq 

def dijkstra(graph, start):
    
    priority_queue = [(0, start)]
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'H': 11, 'C': 8},
    'C': {'B': 8, 'I': 2, 'D': 7},
    'D': {'C': 7, 'I': 4, 'F': 14},
    'E': {'F': 10, 'G': 2},
    'F': {'D': 14, 'E': 10, 'G': 1},
    'G': {'E': 2, 'F': 1, 'H': 6},
    'H': {'A': 8, 'B': 11, 'G': 6},
    'I': {'C': 2, 'D': 4}
}


start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
for vertex, distance in shortest_distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
