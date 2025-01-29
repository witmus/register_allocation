import matplotlib.pyplot as plt
import numpy as np

from experiments import INPUTS

ALGOS = [
    'welshpowell',
    # 'backtracking',
    'dsatur',
    # 'simplify_spill',
    'greedy',
    'tabusearch'
]

def plot_scores(algo: str, n: int, d: int):
    scores = np.load(f'scores/{algo}_{n}_{d}.npy')
    print(np.mean(scores[:,0]) * 1000)
    print(scores[:,1])

for n,d in INPUTS:
    print('nodes = ', n)
    for a in ALGOS:
        print(a)
        scores = np.load(f'scores/{a}_{n}_{d}.npy')
        print(np.mean(scores[:,0]) * 1000)
        print(np.std(scores[:,0]) * 1000)
        print(np.mean(scores[:,1]))
        print('==============')

# plot_scores('tabusearch', 25, 2)
# plot_scores('tabusearch', 50, 4)
# plot_scores('tabusearch', 100, 8)
# plot_scores('tabusearch', 200, 10)
# plot_scores('tabusearch', 400, 12)
