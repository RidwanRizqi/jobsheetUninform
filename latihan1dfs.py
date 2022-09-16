graph = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'F', 'G'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['A', 'F'],
    'F': ['A', 'B', 'E'],
    'G': ['B', 'C', 'H'],
    'H': ['G', 'D']
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Hasil penelusuran graf menggunakan DFS:")
dfs(visited, graph, 'A')
