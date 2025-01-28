from collections import deque
from random import randint

def tabu_search(graph, registers, tabu_size=10, repeats=100, max_iterations=1000):
    colors = list(range(registers))
    result = dict()
    
    for i in range(len(graph)):
        result[i] = colors[randint(0, registers - 1)]

    aspiration = dict()
    tabu = deque()
    counter = 0

    while counter < max_iterations:
        conflicts = 0
        candidates = set()
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph[i][j] >  0:
                    if result[i] == result[j]:
                        candidates.add(i)
                        candidates.add(j)
                        conflicts += 1
        candidates = list(candidates)

        if conflicts == 0:
            break

        next_solution = None
        for _ in range(repeats):
            node = candidates[randint(0, len(candidates) - 1)]
            
            next_color = colors[randint(0, registers - 2)]
            if result[node] == next_color:
                next_color = colors[-1]

            next_solution = dict(result)
            next_solution[node] = next_color
            new_conflicts = 0

            for i in range(len(graph)):
                for j in range(i + 1, len(graph)):
                    if graph[i][j] > 0 and next_solution[i] == next_solution[j]:
                        new_conflicts += 1

            if new_conflicts < conflicts:
                if new_conflicts <= aspiration.setdefault(conflicts, conflicts - 1):
                    aspiration[conflicts] = new_conflicts - 1
                    if (node, next_color) in tabu:
                        tabu.remove((node, next_color))
                        break
                else:
                    if (node, next_color) in tabu:
                        continue
                break

        tabu.append((node, result[node]))
        if len(tabu) > tabu_size:
            tabu.popleft()

        result = next_solution
        counter += 1

    if conflicts != 0:
        print("No coloring found with {} colors.".format(registers))
        return None
    else:
        print("Found coloring:\n", result)
        return result
