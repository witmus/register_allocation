from itertools import combinations
from typing import List

from matplotlib import pyplot as plt
import networkx as nx

def generate_graph(symbols: List[List[str]]) -> nx.Graph :
    G = nx.Graph()
    for s in symbols:
        for c in s:
            G.add_node(c)
        G.add_edges_from(list(combinations(s,2)))
        
    return G