"""
This adheres a solution of Day 8 puzzle PART Two
- https://adventofcode.com/2023/day/8#part2
"""

import math


def parse(n: str) -> set:
    return (lambda a, b: (a, b[1:-1].split(", ")))(*n.split(" = "))


def traverse(instruct: str):
    while True:
        for i in instruct:
            yield 0 if i == "L" else 1


def find_z(n: str, nodes: dict, instruct: str) -> int:
    step, z, cnt = traverse(instruct), n, 0

    while z[-1] != "Z":
        z, cnt = nodes[z][next(step)], cnt + 1

    return cnt


instruct, _, *network = open("data.in").read().split("\n")
nodes = dict([parse(n) for n in network])

travel_n = [n for n in nodes.keys() if n[-1] == "A"]
cnt_z = [find_z(n, nodes, instruct) for n in travel_n]
# interestingly, individuals can be solved separately
# https://github.com/womogenes/AoC-2023-Solutions/blob/main/day_08/day_08_p2.py
steps = math.lcm(*cnt_z)

print(f"[Total Steps Is: {steps}]")
