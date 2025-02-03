import sys
import traceback
import matplotlib.pyplot as plt
import numpy as np

from experiments import GRAPH_SIZES, DENSITIES
from plots import ALGOS

def print_scores(algo: str):
    scores = np.load(f'scores/{algo}.npy')
    print('\hline')
    for s, size in enumerate(GRAPH_SIZES):
        line = str(size) + ' & '
        for d, density in enumerate(DENSITIES):
            if algo == 'backtracking' and d > 1:
                continue
            if scores[s,d,:,0].all() == 0:
                continue

            line += str('%.4f' % (np.mean(scores[s,d,:,0]) * 1000)) + ', ' + str(np.mean(scores[s,d,:,1])) + ' & '
            # print('%.4f' % (np.std(scores[s,d,:,0]) * 1000))
            # print(np.mean(scores[s,d,:,1]))
        print(line[:-3] + ' \\\\')
        print('\\hline')


if __name__ == '__main__':
    try:
        algo = sys.argv[1]
        print_scores(algo)
    except Exception as e:
        traceback.print_exc()