"""
This adheres a solution of Day 8 puzzle
- https://adventofcode.com/2023/day/8
"""


def parse(n: str) -> set:
    node, network = n.split(" = ")
    return (node, network[1:-1].split(", "))


instruct, _, *network = open("data.in").read().split("\n")
nodes = dict([parse(n) for n in network])

travel_n, answer = 'AAA', 0

for node, connected in nodes.items():
    print(f"{node} => {connected}")

    if travel_n == 'ZZZ':
        break

print(f"[Total Steps Is: {answer}]")
