
def prim(graph, start):
    visited = {start}
    cost = 0

    while len(visited) < len(graph):
        edges = [(w, u, v) for u in visited
                 for v, w in graph[u] if v not in visited]

        if not edges:
            print("Graph is disconnected")
            return

        w, u, v = min(edges)
        print(u, "-", v, ":", w)
        visited.add(v)
        cost += w

    print("Total Cost:", cost)


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

prim(graph, 'A')
