from math import sqrt
from time import perf_counter
import numpy as np

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
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'greedy {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = greedy(graph, False)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'greedy {size}-{density} finish')
        np.save(f'scores/greedy', scores)
    except:
        np.save(f'scores/greedy', scores)

def experiment_welsh_powell():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'welshpowell {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = greedy(graph, True)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'welsh-powell {size}-{density} finish')
        np.save(f'scores/welshpowell', scores)
    except:
        np.save(f'scores/welshpowell', scores)

def experiment_backtracking():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'backtracking {size}-{density} start')
                for i in range(NUM_CALLS):
                    colors = int(sqrt(size))
                    while True:
                        start = perf_counter()
                        result = backtracking(graph, colors)
                        stop = perf_counter()
                        if -1 in result.values():
                            print('fail', colors)
                            colors += 1
                        else:
                            scores[s,d,i,0] = stop - start
                            scores[s,d,i,1] = colors
                            break
                print(f'backtracking {size}-{density} finish')
        np.save(f'scores/backtracking', scores)
    except:
        np.save(f'scores/backtracking', scores)

def experiment_dsatur():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'dsatur {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = dsatur(graph)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'dsatur {size}-{density} finish')
        np.save(f'scores/dsatur', scores)
    except:
        np.save(f'scores/dsatur', scores)

def experiment_simpspill():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'simpspill {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = simplify_and_spill(graph)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    scores[s,d,i,1] = max(result.values()) + 1
                print(f'simpspill {size}-{density} finish')
        np.save(f'scores/simpspill', scores)
    except:
        np.save(f'scores/simpspill', scores)

def experiment_tabu():
    scores = np.zeros(shape=(len(GRAPH_SIZES), len(DENSITIES), NUM_CALLS, 2))
    try:
        for s,size in enumerate(GRAPH_SIZES):
            for d,density in enumerate(DENSITIES):
                graph = get_graph(f'inputs/input_{size}_{density}.txt')
                print(f'tabu {size}-{density} start')
                for i in range(NUM_CALLS):
                    start = perf_counter()
                    result = tabu_search(graph, n, int(n/2), n * 2, n * 4)
                    stop = perf_counter()
                    scores[s,d,i,0] = stop - start
                    if result != None:
                        scores[s,d,i,1] = max(result.values()) + 1
                print(f'tabu {size}-{density} finish')
        np.save(f'scores/tabu', scores)
    except:
        np.save(f'scores/tabu', scores)
