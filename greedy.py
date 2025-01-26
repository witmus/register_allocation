from itertools import combinations
from typing import List

from matplotlib import pyplot as plt
import networkx as nx




def greedy(g, r):

    nodes = sorted(g.nodes(), key=lambda x: g.degree(x), reverse=True)
    colors = {}
    neighbor_colors = set()


    for node in nodes:
        #print("\nnode: ")
        #print(node)

        neighbor_colors = set()
        #print("\nneighbor_colors: ")
        #print(neighbor_colors)

        for neighbor in g.neighbors(node):
            #print("\nneighbor: ")
            #print(neighbor)
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])
                #print("\nneighbor colors: ")
                #print(neighbor_colors)

        color = 0

        while color in neighbor_colors:
            color += 1
            if color > r-1:
                print("error: za malo dostepnych rejestrów")
            #print('\ncolor: ')
            #print(color)
        
        colors[node] = color
        #print('\ncolors: ')
        #print(colors)
    
    #print("Kolory: ")
    #print(colors)
    
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

