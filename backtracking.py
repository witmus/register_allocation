import networkx as nx

def _is_valid(am, result, vertex, color):
    for i in range(len(am)):
        if am[vertex][i] and color == result[i]:
            return False
    
    return True

def color_graph(am, r, result, vertex):
    if vertex == len(am):
        return True
    
    for i in range(r):
        if _is_valid(am, result, vertex, i):
            result[vertex] = i
            if color_graph(am, r, result, vertex + 1):
                return True
            
            result[vertex] = -1
    return False


def backtracking(graph, registers):
    result = [-1] * len(graph.nodes())
    print(len(result))
    adjacency_matrix = nx.to_numpy_array(graph)
    print(len(adjacency_matrix))

    color_graph(adjacency_matrix, registers, result, 0)
    
    nodes = list(graph.nodes())
    return {nodes[i]: result[i] for i in range(len(nodes))}
