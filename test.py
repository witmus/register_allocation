import numpy as np
import networkx as nx

from graph_io import read_graph, write_graph
from generate_code import generate_code
from graphgen.get_graph import get_graph
from tabu_search import tabu_search
from greedy import greedy
from dsatur import dsatur
from simplify_spill import simplify_and_spill
# generate_code(123, 3)
# G = get_graph('inputs/input_123_3.txt')
# write_graph(G, 123, 3)

size = 50
rg = read_graph(f'graphs/g_{size}_5')
colors = max(nx.coloring.greedy_color(rg).values())-1

# result = dsatur(rg)
# print(result)
# print(max(result.values()) + 1)

result = tabu_search(rg, colors, size, size * 2, size * 100)

if result != None:
    print('===================\n\n')
    print(colors)
    # print(result)
    print(max(result.values()) + 1)

# print(colors)
# result = simplify_and_spill(rg, colors)
# print(max(result.values()) + 1)
# print(len([x for x in result.values() if x == -1]))
