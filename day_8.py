"""
This adheres a solution of Day 8 puzzle
- https://adventofcode.com/2023/day/8
"""


def parse(n: str) -> set:
    return (lambda a, b: (a, b[1:-1].split(", ")))(*n.split(" = "))


def traverse(instruct: str):
    while True:
        for i in instruct:
            yield 0 if i == "L" else 1


instruct, _, *network = open("data.in").read().split("\n")
nodes = dict([parse(n) for n in network])
travel_n, steps, step = "AAA", 0, traverse(instruct)

while travel_n != "ZZZ":
    print(f"{travel_n} => {nodes[travel_n]}")
    travel_n = nodes[travel_n][next(step)]
    steps += 1

print(f"[Total Steps Is: {steps}]")
