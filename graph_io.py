import networkx as nx

def write_graph(G, size, density):
    nx.write_adjlist(G, f'graphs/g_{size}_{density}')

def read_graph(path):
    return nx.read_adjlist(path)
