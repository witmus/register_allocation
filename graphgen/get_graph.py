import networkx as nx

from graphgen.get_input import get_input
from graphgen.get_symbols import get_symbols
from graphgen.generate_graph import generate_graph

def get_graph(path: str) -> nx.Graph :    
    i = get_input(path)
    s = get_symbols(i)
    return generate_graph(s)