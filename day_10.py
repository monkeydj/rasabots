"""
This adheres a solution of Day 10 puzzle
- https://adventofcode.com/2023/day/10
"""


def find_adjacent_pipes(pipes: list[str], row: int, col: int) -> list[list[int]]:
    adjacents = []

    match pipes[row][col]:
        case '|':
            adjacents.append([row + 1, col], [row - 1, col])
        case '-':
            adjacents.append([row, col + 1], [row, col - 1])
        case 'L':
            adjacents.append([row, col + 1], [row - 1, col])
        case 'J':
            adjacents.append([row, col - 1], [row - 1, col])
        case '7':
            adjacents.append([row, col - 1], [row + 1, col])
        case 'F':
            adjacents.append([row, col + 1], [row + 1, col])
        case _:  # it must be ground
            pass

    return adjacents


def trace_pipes(s_x: int, s_y: int, pipe_maze: list[str]) -> int:
    pass


pipe_maze = open("data.in").read().split()
s_point = None

for i, p in enumerate(pipe_maze):
    for j in range(len(p)):
        if p[j] == 'S':
            s_point = [i, j]
            break

    if s_point:
        break  # found S, start tracing


print("Starting point", s_point)
print(f"[Farthest Step Is: {0}]")
