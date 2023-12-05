# Promgram to Understand Bellman-Ford Algorithm for Negative -weighted graph
def bellman_ford(graph, start):
    distance = {vertex: float('infinity') for vertex in graph}
    predecessor = {vertex: None for vertex in graph}
    distance[start] = 0
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
                    predecessor[neighbor] = vertex
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] + weight < distance[neighbor]:
                print("Graph contains a negative cycle")
                return

    
    print("Vertex Distance from Source Predecessor")
    for vertex in graph:
        print(f"{vertex}\t\t{distance[vertex]}\t\t\t{predecessor[vertex]}")


sample_graph = {
    'A': [('B', 6), ('C', 7)],
    'B': [('D', 5), ('E', -4), ('C', 8)],
    'C': [('E', 9), ('D', -3)],
    'D': [('B', -2)],
    'E': [('A', 2), ('D', 7)]
}

bellman_ford(sample_graph, 'A')

