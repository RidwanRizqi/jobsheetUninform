graph = {
    'A': ['B'],
    'B': ['A', 'F', 'G'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['F'],
    'F': ['B', 'E'],
    'G': ['B', 'C'],
    'H': ['D']
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        if node == 'D':
            print("Nilai D Sudah Ditemukan Program Dihentikan")
            return
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Hasil penelusuran graf menggunakan DFS:")
dfs(visited, graph, 'A')
