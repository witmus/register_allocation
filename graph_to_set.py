def graph_to_set(g):
    graph = {}
    for n, neighbors in g.adjacency():
        graph[n] = set()
        for neighbor in neighbors:
            graph[n].add(neighbor)
    return graph