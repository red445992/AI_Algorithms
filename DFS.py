def DFS(graph,root):
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D'],
    'D': ['C'],
    'E': ['A', 'B'],
    'F': ['B'],
    'G': ['D'],
    'H': ['F', 'G']
}
result = DFS(graph,'A')
print(result)