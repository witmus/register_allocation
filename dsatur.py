from graph_to_set import graph_to_set


def dsatur(g):
    result = dict.fromkeys(g.nodes())
    uncolored_vertices = []
    max_degree_node = ""

    max_degree = -1
    graph = graph_to_set(g)
    for node, neighbors in graph.items():
        if len(neighbors) > max_degree:
            max_degree = len(neighbors)
            max_degree_node = node

    result[max_degree_node] = 0

    saturations = {node : 0 for node in graph}

    for neighbor in graph[max_degree_node]:
        saturations[neighbor] += 1

    saturations[max_degree_node] = float('-inf')

    for node in graph:
        if node != max_degree_node:
            result[node] = -1
            uncolored_vertices.append(node)

    while uncolored_vertices:
        used_colors = []
        current_node = ""
        saturation = -1

        for node, level in saturations.items():
            if level > saturation:
                saturation = level
                current_node = node
                used_colors = [result[neighbor] for neighbor in graph[node]]

        uncolored_vertices.remove(current_node)

        next_color = -1

        for c in range(max(used_colors)):
            if c not in used_colors:
                next_color = c

        if next_color == -1:
            next_color = max(used_colors) + 1

        result[current_node] = next_color

        for neighbor in graph[current_node]:
            if saturations[neighbor] != float('-inf'):
                saturations[neighbor] += 1

        saturations[current_node] = float('-inf')

    return result
