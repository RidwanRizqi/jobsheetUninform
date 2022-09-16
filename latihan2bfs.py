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

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)

        print(s, end=" ")
        if s == 'D':
            print("Nilai D sudah ditemukan program dihentikan")
            break

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Hasil penelusuran graf menggunakan BFS:")
bfs(visited, graph, 'A')
