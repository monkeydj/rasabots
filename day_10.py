"""
This adheres a solution of Day 10 puzzle
- https://adventofcode.com/2023/day/10
"""

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
