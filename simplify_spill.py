def simplify_and_spill(edges, num_registers):

    graph = {}
    for edge_group in edges:
        for node in edge_group:
            if node not in graph:
                graph[node] = set()
            for neighbor in edge_group:
                if neighbor != node:
                    graph[node].add(neighbor)

    stack = []
    temp_graph = {node: set(neighbors) for node, neighbors in graph.items()}
    spilled = set()

    while temp_graph:
        low_degree_node = None
        for node, neighbors in temp_graph.items():
            if len(neighbors) < num_registers:
                low_degree_node = node
                break

        if low_degree_node is not None:
            stack.append(low_degree_node)
            for neighbor in temp_graph[low_degree_node]:
                temp_graph[neighbor].remove(low_degree_node)
            del temp_graph[low_degree_node]
        else:
            spill_node = next(iter(temp_graph))
            spilled.add(spill_node)
            del temp_graph[spill_node]

    colors = {}
    while stack:
        node = stack.pop()
        neighbor_colors = {colors[neighbor] for neighbor in graph[node] if neighbor in colors}
        for register in range(num_registers):
            if register not in neighbor_colors:
                colors[node] = register
                break
        else:
            colors[node] = "spill"
            spilled.add(node)

    for node in spilled:
        colors[node] = "spill"

    return colors


# if __name__ == "__main__":
#     example_graph = [
#         ["A", "B", "C"],
#         ["B", "D"],
#         ["C", "D", "E"],
#         ["E", "F"]
#     ]
#
#     num_registers = 3
#
#     allocation = simplify_and_spill(example_graph, num_registers)
#
#     print("Przypisanie rejestrów:")
#     for node, register in allocation.items():
#         print(f"Wierzchołek {node}: {register}")
