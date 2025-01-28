import sys
from random import randint

def generate(vars=100, density=10):
    f = open(f'input_{vars}_{density}.txt', 'a')
    for v in range(vars):
        expr = 'x' + str(v) + ' = '
        for d in range(density):
            expr += 'x' + str(randint(0, vars - 1)) + ' +'
        expr = expr[:-1]
        expr += '\n'
        f.write(expr)
    f.close()

if __name__ == '__main__':
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    generate(n,d)