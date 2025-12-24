from collections import deque

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def next_move_part1(current, move):
    next = [elm for elm in current]
    for pos in move:
        next[int(pos)] = not next[int(pos)]
    return tuple(next)


def minimum_moves_part1(target, moves):
    visited = set()
    queue = deque()
    queue.append(tuple([False for _pos in target]))
    visited.add(queue[0])
    res = 0
    while len(queue) > 0:
        res += 1
        n = len(queue)
        for _ in range(n):
            current = queue.popleft()
            for move in moves:
                next = next_move_part1(current, move)
                if next == target:
                    return res
                if next not in visited:
                    visited.add(next)
                    queue.append(next)
    raise Exception("no solution")


def minimum_moves_part2(target, moves):
    n_positions = len(target)
    n_moves = len(moves)

    # Build constraint matrix: A[position][move] = 1 if move affects position
    A = np.zeros((n_positions, n_moves))
    for m_idx, move in enumerate(moves):
        for pos in move:
            A[int(pos)][m_idx] = 1

    # Objective: minimize sum of x (total number of moves)
    c = np.ones(n_moves)

    # Constraints: A @ x = target (each position reaches exactly its target)
    b = np.array([int(t) for t in target])
    constraints = LinearConstraint(A, b, b)

    # Bounds: x >= 0
    bounds = Bounds(0, np.inf)

    # All variables must be integers
    integrality = np.ones(n_moves)

    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        return int(round(result.fun))
    else:
        raise Exception("no solution")


part1_total = 0
part2_total = 0
for line in open("input.txt", "r"):
    [target, rest_of_line] = line.rstrip("\n").split("]")
    target = tuple(False if c == "." else True for c in target[1:])
    [moves, joltages] = rest_of_line.split("{")
    moves = [move.strip("()").split(",") for move in moves.strip().split(" ")]
    joltages = joltages.split(",")
    joltages[-1] = joltages[-1][:-1]  # remove trailing }
    joltages = tuple([int(joltage) for joltage in joltages])
    part1_total += minimum_moves_part1(target, moves)
    part2_total += minimum_moves_part2(joltages, moves)
print(f"part1 total: {part1_total}\npart2 total: {part2_total}")
