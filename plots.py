import sys
import matplotlib.pyplot as plt
import numpy as np

from experiments import GRAPH_SIZES, DENSITIES

ALGOS = [
    'greedy',
    'welshpowell',
    'dsatur',
    'simpspill',
    # 'backtracking',
    # 'tabu'
]

def plot_time_on_nodes(points: int = 22):
    plt.figure(figsize=(16,9))
    plt.title('Uśredniony czas wykonania')
    plt.xlabel('Liczba zmiennych')
    plt.ylabel('Czas [ms]')
    plt.yscale('log')
    plt.xscale('log')
    for a, alg in enumerate(ALGOS):
        scores = np.load(f'scores/{alg}.npy')
        plt.plot(GRAPH_SIZES[:points], np.array([np.mean(x) for x in scores[:,:,:,0]])[:points], 'o-', label=alg)
    plt.legend()
    plt.show()
    plt.close()

def plot_colors_on_nodes(points: int = 22):
    plt.figure(figsize=(16,9))
    plt.title('Uśredniona liczba użytych kolorów')
    plt.xlabel('Liczba zmiennych')
    plt.ylabel('Liczba kolorów')
    plt.xscale('log')
    for a, alg in enumerate(ALGOS):
        scores = np.load(f'scores/{alg}.npy')

        x = GRAPH_SIZES[:points]
        y = np.array([np.mean(x) for x in scores[:,:,:,1]])

        plt.plot(x, y[:points], 'o-', label=alg)
    plt.legend()
    plt.show()
    plt.close()

if __name__ == '__main__':
    # plot_time_on_nodes()
    # plot_time_on_nodes(5)
    # plot_time_on_nodes(8)
    plot_time_on_nodes(17)

    # plot_colors_on_nodes()
    # plot_colors_on_nodes(5)
    # plot_colors_on_nodes(8)
    # plot_colors_on_nodes(17)
