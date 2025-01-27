import networkx as nx

def dynamic(g: nx.Graph, r: int):
    print(g.nodes)
    print(g.edges)
    
    for n,nd in g.adjacency():
        print(n)
        print(list(nd.keys()))
        print('=============')
