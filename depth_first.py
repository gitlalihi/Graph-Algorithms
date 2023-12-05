#Program to print DFS traversal from a given  graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=' ')
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}


dfs(graph, 0)
