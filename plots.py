import sys
import matplotlib.pyplot as plt
import numpy as np

from experiments import GRAPH_SIZES, DENSITIES

ALGOS = [
    'welshpowell',
    # 'backtracking',
    # 'dsatur',
    # 'simpspill',
    # 'greedy',
    # 'tabusearch'
]

def plot_scores(algo: str):
    scores = np.load(f'scores/{algo}.npy')
    for d, density in enumerate(DENSITIES):
        for s, size in enumerate(GRAPH_SIZES):
            print(algo, size, density)
            print(np.mean(scores[s,d,:,0]) * 1000)
            print(np.std(scores[s,d,:,0]) * 1000)
            print(np.mean(scores[s,d,:,1]))
            if algo == 'simpspill':
                print(np.mean(scores[s,d,:,2]))

if __name__ == '__main__':
    try:
        algo = sys.argv[1]
        plot_scores(algo)
    except:
        for a in ALGOS:
            plot_scores(a)
