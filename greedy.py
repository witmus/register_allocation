from random import shuffle

def greedy(g, r, is_welsh_powell=True):
    nodes = list(g.nodes())
    if is_welsh_powell:
        nodes = sorted(nodes, key=lambda x: g.degree(x), reverse=True)
    else:
        shuffle(nodes)
    
    colors = {}
    neighbor_colors = set()

    for node in nodes:
        neighbor_colors = set()

        for neighbor in g.neighbors(node):
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])

        color = 0

        while color in neighbor_colors:
            color += 1
            if color > r-1:
                print("error: za malo dostepnych rejestrów")
        
        colors[node] = color
    
    return colors

"""
def generate_graph(symbols: List[List[str]]) -> nx.Graph :
    G = nx.Graph()
    for s in symbols:
        for c in s:
            G.add_node(c)
        G.add_edges_from(list(combinations(s,2)))
        
    return G


symbols = [["A", "B", "C"], ["B", "D"], ["C", "D", "E"], ["E", "F"]]
G = generate_graph(symbols)
coloring = greedy(G, 6)

print("Kolory wierzchołków:", coloring)



    print("\ng: ")
    print(g)

    print("\nr: ")
    print(r)

    print("\ng.edges: ")
    print(g.edges)

    print("\ng.degree: ")
    print(g.degree)

    print("\nsorted(g.nodes(), key=lambda x: g.degree(x), reverse=True)")
    print(sorted(g.nodes(), key=lambda x: g.degree(x), reverse=True))

"""
