from math import sqrt
from time import perf_counter
import numpy as np
import networkx as nx

from graph_io import read_graph
from graphgen.get_graph import get_graph

from backtracking import backtracking
from dsatur import dsatur
from greedy import greedy
from simplify_spill import simplify_and_spill
from tabu_search import tabu_search

GRAPH_SIZES = [
    12, 25, 50, 100, 150, 200, 300, 400, 500, 750,
    1_000, 1_500, 2_000, 5_000, 10_000, 25_000, 50_000, 75_000,
    100_000, 250_000, 500_000, 1_000_000
]

DENSITIES = [
    2, 3, 4, 5
]

NUM_CALLS = 10

def experiment_greedy():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                print(f'greedy {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = greedy(graph, False)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'greedy {size}-{density} finish')
    finally:
        np.save(f'scores/greedy', scores)

def experiment_welsh_powell():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                print(f'welshpowell {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = greedy(graph, True)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'welsh-powell {size}-{density} finish')
    finally:
        np.save(f'scores/welshpowell', scores)

def experiment_backtracking():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                print(f'backtracking {size}-{density} start')
                for i in range(NUM_CALLS):
                    colors = max(nx.greedy_color(graph).values()) + 1
                    start = perf_counter()
                    result = backtracking(graph, colors)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'backtracking {size}-{density} finish')
                np.save(f'scores/backtracking_checkpoint', scores)
        np.save(f'scores/backtracking', scores)
    finally:
        np.save(f'scores/backtracking', scores)

def experiment_dsatur():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                print(f'dsatur {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = dsatur(graph)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'dsatur {size}-{density} finish')
                np.save('dsatur_checkpoint', scores)
    finally:
        np.save(f'scores/dsatur', scores)

def experiment_simpspill():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 3))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                colors = max(nx.greedy_color(graph).values())
                if size <= 10000:
                    colors += 1
                else:
                    colors += 2
                print(f'simpspill {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = simplify_and_spill(graph, colors)
                    rvals = result.values()
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(rvals) + 1
                    scores[s,d,i,2] = len([x for x in rvals if x == -1]) / size
                print(f'simpspill {size}-{density} finish')
                np.save('scores/simpspill_checkpoint', scores)
        np.save(f'scores/simpspill', scores)
    finally:
        print('saving simpsill')
        np.save(f'scores/simpspill', scores)

def experiment_tabu():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = read_graph(f'graphs/g_{size}_{density}')
                colors = max(nx.greedy_color(graph).values()) + 1
                print(f'tabu {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = tabu_search(graph, colors, density * 5, density * 50, density * 200)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    if result != None:
                        scores[s,d,i,1] = max(result.values()) + 1
                print(f'tabu {size}-{density} finish {np.mean(scores[s,d,:,1])}')
                np.save(f'scores/tabu_checkpoint', scores)
    finally:
        np.save(f'scores/tabu', scores)
