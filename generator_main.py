from generate_code import generate_code
from experiments import GRAPH_SIZES, DENSITIES

for size in GRAPH_SIZES:
    for density in DENSITIES:
        generate_code(size, density)
