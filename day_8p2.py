"""
This adheres a solution of Day 8 puzzle PART Two
- https://adventofcode.com/2023/day/8#part2
"""


def parse(n: str) -> set:
    return (lambda a, b: (a, b[1:-1].split(", ")))(*n.split(" = "))


def traverse(instruct: str):
    while True:
        for i in instruct:
            yield 0 if i == "L" else 1


instruct, _, *network = open("data.in").read().split("\n")
nodes = dict([parse(n) for n in network])
travel_n = [n for n in nodes.keys() if n[-1] == "A"]
steps, step = 0, traverse(instruct)

while True:
    lr, steps = next(step), steps + 1
    print(f"{travel_n}", end=f" =[{lr}]=> ")

    travel_n = [nodes[n][lr] for n in travel_n]
    print(travel_n)

    if sum(1 for n in travel_n if n[-1] == "Z") == len(travel_n):
        break


print(f"[Total Steps Is: {steps}]")
