import sys
from random import sample

def generate_code(vars=100, density=3):
    path = f'inputs/input_{vars}_{density}.txt'
    f = open(path, 'a')
    for v in range(vars):
        expr = 'x' + str(v) + ' = '
        var_nums = sample(range(0,vars), density)
        for var_num in var_nums:
            expr += 'x' + str(var_num) + ' + '
        expr = expr[:-2]
        expr += '\n'
        f.write(expr)
    f.close()
    return path

if __name__ == '__main__':
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    generate_code(n,d)
    