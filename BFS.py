from collections import deque

def BFS(graph,root):
    queue = deque([root])
    visited = set([root])

    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return traversal_order

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
result = BFS(graph,'A')
print(result)