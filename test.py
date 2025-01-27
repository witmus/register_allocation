import networkx as nx
import matplotlib.pyplot as plt

from graphgen.get_graph import get_graph

from dynamic import dynamic

g = get_graph('input.txt')

dynamic(g, 5)
