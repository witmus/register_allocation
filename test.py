import networkx as nx
import matplotlib.pyplot as plt

from networkx.algorithms import greedy_color
from graphgen.get_graph import get_graph

from tabu_search import tabu_search

g = get_graph('input_50_10.txt')

# from simplify_spill import simplify_and_spill
# result = simplify_and_spill(g, 20)
# print(max(result.values()))

# from greedy import greedy
# result_wp = greedy(g,20, True)
# result_greedy = greedy(g,20,False)
# print(max(result_wp.values()))
# print(max(result_greedy.values()))


from backtracking import backtracking

result = backtracking(g,20)
print(result)
print(max(result.values()))

# m = nx.to_numpy_array(g)
# result = tabu_search(m,7,10,1000)
# print(max(result.values()))

# from dsatur import dsatur
# coloring = dsatur(g)
# print(max(coloring.values()))