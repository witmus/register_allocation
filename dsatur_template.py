from graph_to_set import graph_to_set


def dsatur(g, r):
    todo = []
    max_degree = ""
    degree = -1
    result = dict.fromkeys(g.nodes())

    graph = graph_to_set(g)
    for node, neighbors in graph.items():
        if len(neighbors) > degree:
            degree = len(neighbors)
            max_degree = node

    result[max_degree] = 0

    saturation_level = {node: 0 for node in graph}

    for neighbor in graph[max_degree]:
        saturation_level[neighbor] += 1

    saturation_level[max_degree] = float('-inf')

    for node in graph:
        if node != max_degree:
            result[node] = -1
            todo.append(node)

    while todo:
        saturation = -1
        saturation_name = ""
        saturation_colors = []

        for node, level in saturation_level.items():
            if level > saturation:
                saturation = level
                saturation_name = node
                saturation_colors = [result[neighbor] for neighbor in graph[node]]

        if saturation_name == "":
            print("Error: Could not find a max saturated node in the graph (reason unknown)")
            result = {}
            return result

        todo.remove(saturation_name)

        lowest_color = 0
        done = False
        while not done:
            done = True
            for color in saturation_colors:
                if color == lowest_color:
                    lowest_color += 1
                    done = False

        result[saturation_name] = lowest_color

        for neighbor in graph[saturation_name]:
            if saturation_level[neighbor] != float('-inf'):
                saturation_level[neighbor] += 1

        saturation_level[saturation_name] = float('-inf')

    return result
