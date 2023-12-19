"""
This adheres a solution of Day 9 puzzle
- https://adventofcode.com/2023/day/9
"""


def diff(values: list[int]) -> list[int]:
    return [values[i+1] - v for i, v in enumerate(values[:-1])]


def traverse(history: str):
    stacks = [list(map(int, history.split()))]

    while True:
        diff_v = diff(stacks[-1])
        if all(s == 0 for s in diff_v):
            break  # once it reaches the end
        stacks.append(diff_v)

    return sum(s[-1] for s in stacks[::-1])


histories = open("data.in").read().split("\n")
preds_n = [traverse(h) for h in histories]

print(f"[Total Steps Is: {sum(preds_n)}]")
