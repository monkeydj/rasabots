"""
This adheres a solution of Day 9 puzzle PART Two
- https://adventofcode.com/2023/day/9#part2
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

    back_n = 0
    for s in stacks[::-1]:
        back_n = s[0] - back_n

    return back_n


histories = open("data.in").read().split("\n")
preds_n = [traverse(h) for h in histories]

print(f"[Extrapolated Prev. Value Is: {sum(preds_n)}]")
