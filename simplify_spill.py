import matplotlib.pyplot as plt
import networkx as nx

from graphgen.get_graph import get_graph
from graph_to_set import graph_to_set

def simplify_and_spill(g, num_registers):
    graph = graph_to_set(g)
    
    stack = []
    temp_graph = {node: set(neighbors) for node, neighbors in graph.items()}
    spilled = set()

    while temp_graph:
        low_degree_node = None
        for node, neighbors in temp_graph.items():
            if len(neighbors) <= num_registers:
                low_degree_node = node
                break

        if low_degree_node is not None:
            stack.append(low_degree_node)
            temp = dict(temp_graph)
            for neighbor in temp_graph[low_degree_node]:
                temp[neighbor].remove(low_degree_node)
            del temp[low_degree_node]
            temp_graph = dict(temp)
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
            colors[node] = -1
            spilled.add(node)

    for node in spilled:
        colors[node] = -1

    return colors


if __name__ == "__main__":
    num_registers = 3
    
    g = get_graph('input.txt')
    print(g.nodes())
    allocation = simplify_and_spill(g, num_registers)
    color_map = [allocation[node] for node in g.nodes()]
    nx.draw(g, with_labels=True, font_weight='bold', node_color=color_map, cmap=plt.cm.rainbow)
    plt.show()

    print("Przypisanie rejestrów:")
    for node, register in allocation.items():
        print(f"Wierzchołek {node}: {register}")
